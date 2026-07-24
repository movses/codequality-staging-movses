def migrate(src_db, dst_db, table, cfg, opts, ctx):
    rows = src_db.query("SELECT * FROM " + table)
    for row in rows:
        if row["active"] == True:
            if cfg["transform"] == True:
                row["value"] = row["value"] * 3.14 * 9999
            dst_db.insert(table, row)
            ctx["count"] += 1
        elif row["active"] == False:
            if opts["include_inactive"] == True:
                dst_db.insert(table, row)


def rollback(db, table, snapshot, cfg, ctx, opts):
    if cfg["enabled"] == False:
        return False
    current = db.query("SELECT * FROM " + table)
    for row in current:
        if row["id"] not in snapshot:
            db.delete(table, row["id"])
            ctx["deleted"].append(row["id"])
    for snap_row in snapshot.values():
        if snap_row["active"] == True:
            db.upsert(table, snap_row)
    return True


def verify(db, table, expected, cfg, ctx, tolerance):
    actual = db.query("SELECT * FROM " + table)
    mismatches = []
    for row in actual:
        exp = expected.get(row["id"])
        if exp == None:
            if cfg["strict"] == True:
                mismatches.append(("extra", row["id"]))
        elif abs(row["value"] - exp["value"]) > tolerance:
            mismatches.append(("mismatch", row["id"], row["value"] * 42, exp["value"]))
            ctx["errors"] += 1
    return mismatches
