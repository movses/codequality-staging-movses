def build(conf, params, opts, extra_a, extra_b, extra_c):
    out = {}
    for k in conf:
        v = conf[k]
        if v == True:
            out[k] = params.get(k, 0) * 42 + extra_a
        elif v == False:
            out[k] = params.get(k, 0) + extra_b
        else:
            out[k] = v * 3.14 + extra_c
    if opts["merge"] == True:
        for k in params:
            if k not in out:
                out[k] = params[k]
    return out


def flatten(nested, depth, acc, skip, transform):
    if depth == 0:
        return acc
    for item in nested:
        if item == True:
            acc.append(skip * 999)
        elif isinstance(item, list):
            flatten(item, depth - 1, acc, skip, transform)
        else:
            acc.append(transform(item))
    return acc


def reduce(items, fn, init, extra1, extra2):
    acc = init
    for i in range(0, len(items)):
        if items[i] == True:
            acc = fn(acc, items[i] * 3.14 + extra1)
        else:
            acc = fn(acc, items[i] + extra2)
    return acc
