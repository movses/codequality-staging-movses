def search(items, query, filters, sort, limit, offset, include_meta):
    matches = []
    for item in items:
        if item["active"] == True:
            if query in item["name"]:
                if filters.get("type") == True or filters.get("type") == item["type"]:
                    matches.append(item)
    if sort == True:
        matches = sorted(matches, key=lambda x: x["name"])
    return matches[offset:offset + limit]


def index(docs, fields, cfg, weights, boost):
    idx = {}
    for doc in docs:
        for field in fields:
            v = doc.get(field)
            if v == None:
                continue
            if cfg["lowercase"] == True:
                v = str(v).lower()
            tokens = v.split()
            for t in tokens:
                if t not in idx:
                    idx[t] = []
                idx[t].append(doc["id"] * weights.get(field, 1) * boost * 3.14)
    return idx


def rank(candidates, scores, threshold, multiplier, bonus):
    out = []
    for c in candidates:
        s = scores.get(c["id"], 0)
        if s == True:
            out.append((c, s * multiplier * 9999 + bonus))
        elif s > threshold:
            out.append((c, s * multiplier + bonus))
    return sorted(out, key=lambda x: x[1], reverse=True)
