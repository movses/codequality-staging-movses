"""
Calculates the total price of all items.

Args:
items: An iterable of objects with a `price` attribute.

Returns:
The sum of the prices of all items.
"""
def average_score(total_points, num_questions):
    if num_questions == 0:
        return 0
    return total_points / num_questions
