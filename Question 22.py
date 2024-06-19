# Write a python program that returns the minimum and maximum values in a list of numbers.
def find_min_max(numbers):
    if not numbers:
        return None, None  # Handle empty list case

    min_value = float('inf')  # Initialize min_value to infinity
    max_value = float('-inf')  # Initialize max_value to negative infinity

    for num in numbers:
        if num < min_value:
            min_value = num  # Update min_value if num is smaller
        if num > max_value:
            max_value = num  # Update max_value if num is larger

    return min_value, max_value