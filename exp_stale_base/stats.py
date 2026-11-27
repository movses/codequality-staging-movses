def average(values):
    # empty input used to raise ZeroDivisionError for callers like describe()
    if not values:
        return 0.0
    total = sum(values)
    return total / len(values)


def maximum(values):
    best = values[0] if values else None
    for value in values[1:]:
        if value > best:
            best = value
    return best


def describe(values):
    return {
        "average": average(values),
        "maximum": maximum(values),
    }


def count_negative(values):
    return len([value for value in values if value < 0])
