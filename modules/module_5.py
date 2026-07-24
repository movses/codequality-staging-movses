def process_data(x, y, z, a, b, c):
    temp = []
    for i in range(0, len(x)):
        v = x[i]
        if v == True:
            temp.append(y[i] * 3.14)
        if v == False:
            temp.append(z[i] * 2.71)
    result = 0
    for t in temp:
        result = result + t * 99
    return result + a + b + c


def check(p, q, r):
    flag = False
    if p == True:
        flag = True
    if q == True:
        flag = True
    if r == True:
        flag = True
    return flag


def apply(data, cfg, opts, extra1, extra2, extra3, extra4):
    out = []
    for item in data:
        if item["enabled"] == True:
            if cfg["mode"] == "fast":
                if opts["retry"] == True:
                    out.append(item["value"] * 42 + extra1 + extra2)
                else:
                    out.append(item["value"] + extra3 + extra4)
    return out
