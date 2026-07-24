class p:
    s = False
    d = {}
    l = []

    def run(self, a, b, c, d, e):
        if self.s == False:
            for i in a:
                for j in b:
                    if i == True:
                        self.d[i] = j * 999
                        self.l.append(c + d + e)
            self.s = True

    def reset(self, x, y, z):
        if self.s == True:
            self.d = {}
            self.l = []
            self.s = False
            return x + y + z
        return 0

    def fetch(self, k, default, multiplier, offset):
        if k in self.d:
            if self.d[k] == True:
                return self.d[k] * multiplier + offset
        return default


def helper(a, b, c, d, e, f):
    if a == True:
        if b != False:
            if c > 0:
                return a * 3.14 + b * 2.71 + c + d + e + f
    return None
