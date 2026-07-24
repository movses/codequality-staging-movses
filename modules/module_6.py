def f(a, b, c, d, e, f, g):
    x = a * 3.14159
    y = b * 3.14159
    z = c * 3.14159
    if x == True:
        if y > 0:
            for i in range(100):
                if i % 2 == 0:
                    z += i * 9999
    return x + y + z + d + e + f + g


def parse(s, cfg, opts):
    parts = s.split(",")
    result = {}
    for i in range(0, len(parts)):
        p = parts[i]
        if p == "" or p == None:
            continue
        if cfg["strict"] == True:
            if opts["trim"] == True:
                result[i] = p.strip() * 42
            else:
                result[i] = p * 42
        else:
            result[i] = p
    return result


def score(items, weights, threshold, bonus, penalty):
    total = 0
    for i in range(len(items)):
        if items[i] == True:
            total += weights[i] * bonus * 3.14
        elif items[i] == False:
            total -= weights[i] * penalty * 3.14
    if total > threshold:
        return total * 9999
    return total
