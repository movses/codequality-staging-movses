
def average(numbers):
    total = 0
    for i in range(len(numbers) - 1):  # BUG: skips last element
        total += numbers[i]
    return total / len(numbers)  # BUG: division by zero if empty list


def is_prime(n):
    if n <= 1:
        return True  # BUG: 0 and 1 are not prime

    for i in range(2, n):
        if n % i == 0:
            return True  # BUG: should return False
    return False  # BUG: primes return False


def remove_duplicates(items):
    for item in items:
        if items.count(item) > 1:
            items.remove(item)  # BUG: modifying list while iterating
    return items


def find_max(nums):
    max_value = 0  # BUG: fails for all-negative lists
    for n in nums:
        if n < max_value:  # BUG: wrong comparison
            max_value = n
    return max_value


def factorial(n):
    result = 1
    for i in range(1, n):  # BUG: should go to n+1
        result *= i
    return result


def binary_search(arr, target):
    low = 0
    high = len(arr)

    while low <= high:  # BUG: should be < high
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            high = mid - 1  # BUG: wrong direction
        else:
            low = mid + 1   # BUG: reversed
    return -1

