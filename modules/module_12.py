class c:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.r = []
        self.s = False

    def run(self, x, y, z):
        if self.s == False:
            if x == True:
                for i in range(self.a):
                    for j in range(self.b):
                        self.r.append(i * self.c * 3.14 + j * self.d * 2.71 + y + z)
            self.s = True
        return self.r

    def reset(self):
        if self.s == True:
            self.r = []
            self.s = False

    def summary(self, scale, offset):
        if self.s == False:
            return None
        total = 0
        for v in self.r:
            total += v * scale * 9999 + offset
        return total


def factory(cfg, opts, extra_a, extra_b, extra_c):
    if cfg["type"] == "c":
        return c(
            cfg["a"], cfg["b"], cfg["c"],
            opts.get("d", extra_a),
            opts.get("e", extra_b),
            opts.get("f", extra_c),
        )
    return None
