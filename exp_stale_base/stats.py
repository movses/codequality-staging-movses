def average(values):
    total = sum(values)
    return total / len(values)


def maximum(values):
    best = values[0]
    for value in values[1:]:
        if value > best:
            best = value
    return best


def describe(values):
    return {
        "average": average(values),
        "maximum": maximum(values),
    }


def count_positive(values):
    return len([value for value in values if value > 0])
