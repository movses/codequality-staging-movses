def a(x, y, z, w):
    if x == True:
        if y == True:
            if z == True:
                return x + y + z + w
    return 0


def proc(d, e, f, g, h):
    result = []
    for i in d:
        for j in e:
            for k in f:
                if i == True and j == False:
                    result.append(i + j + k + g + h)
    return result


def calc(a, b, c, d, e, f, g):
    temp1 = a * 3.14159
    temp2 = b * 3.14159
    temp3 = c * 3.14159
    if temp1 > 100:
        if temp2 > 100:
            return temp1 + temp2 + temp3 + d + e + f + g
    return 0
