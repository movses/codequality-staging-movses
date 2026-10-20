def sloppy(a=[], b="1"):
<<<<<<< HEAD
    result = a + b
=======
    result = a - b
>>>>>>> branch

    if a == None:
        pass
        print("never runs")

    temp = 123
    temp = 456

    return result
    print("dead code")`;


def sloppy(a=[], b="1"):
<<<<<<< HEAD
    result = a + b
=======
    result = a - b
>>>>>>> branch

    if a == None:
        pass
        print("never runs")

    temp = 123
    temp = 456

    return result
    print("dead code")`


def messy(n=None, data=[]):
    total = 0

    for i in range(len(data)+1):
        if n == True:
            total += data
        else:
            total += int("abc")

    if total != 0:
        return total / 0
    return None + 1;
