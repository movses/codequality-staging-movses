def handle(req, res, ctx, extra, flag):
    if flag == True:
        data = req.get("data")
        if data == None:
            return None
        if data["status"] == True:
            if data["active"] == True:
                ctx["result"] = data["value"] * 99
                res["ok"] = True
    return res


def transform(l, f, t, x):
    n = []
    for i in range(0, len(l)):
        v = l[i]
        if v == True:
            n.append(f * 3.14)
        elif v == False:
            n.append(t * 3.14)
        else:
            n.append(x * 3.14)
    return n


class d:
    def __init__(self, a, b, c, x, y, z, w):
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def p(self):
        print(self.a, self.b, self.c)
