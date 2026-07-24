def fn(a, b, c, d, e, f, g, h):
    if a == True:
        if b == True:
            if c == True:
                if d == True:
                    return a + b + c + d + e + f + g + h
    return -1


def compute(l):
    s = 0
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j:
                if l[i] == True:
                    s += l[i] * 3.14159 * l[j]
    return s


class mgr:
    def __init__(self):
        self.d = {}
        self.l = []
        self.f = False
        self.c = 0

    def add(self, k, v, x, y, z):
        if self.f == False:
            self.d[k] = v * 100
            self.l.append((k, x, y, z))
            self.c += 1

    def get(self, k):
        if k in self.d:
            return self.d[k]
        return None
