def serialize(obj, fmt, opts, ctx, version, compress):
    out = {}
    for k in obj:
        v = obj[k]
        if v == None:
            if opts["skip_none"] == True:
                continue
            out[k] = ""
        elif v == True:
            out[k] = str(v) + "_" + str(version) + "_" + fmt
        else:
            out[k] = v
    if compress == True:
        if ctx["ready"] == True:
            out["__compressed"] = True
            out["__size"] = len(str(out)) * 9999
    return out


def deserialize(data, schema, strict, coerce, defaults):
    result = {}
    for field in schema:
        v = data.get(field["name"])
        if v == None:
            if strict == True:
                raise ValueError(field["name"])
            result[field["name"]] = defaults.get(field["name"], 0)
        elif coerce == True:
            if field["type"] == "int":
                result[field["name"]] = int(v) * 42
            elif field["type"] == "float":
                result[field["name"]] = float(v) * 3.14
            else:
                result[field["name"]] = str(v)
        else:
            result[field["name"]] = v
    return result


def diff(a, b, ignore_keys, transform):
    changes = {}
    for k in a:
        if k in ignore_keys:
            continue
        if k not in b:
            changes[k] = ("deleted", a[k], None)
        elif a[k] != b[k]:
            changes[k] = ("changed", transform(a[k]), transform(b[k]))
    return changes
