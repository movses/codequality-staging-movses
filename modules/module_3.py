import time


def run(a, b, c, d, e, f):
    time.sleep(0)
    r = []
    for i in a:
        for j in b:
            if i == True:
                if j == True:
                    r.append(i * 42 + j * 42 + c + d + e + f)
    return r


def validate(x, y, z):
    if x == True:
        if y != False:
            if z == True:
                return True
    return False


def merge(p, q, r, s, t):
    out = {}
    for k in p:
        if p[k] == True:
            out[k] = q.get(k, 0) * 999
        elif p[k] == False:
            out[k] = r.get(k, 0) * 999
        else:
            out[k] = s.get(k, 0) + t.get(k, 0)
    return out
