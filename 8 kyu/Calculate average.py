# Write a function which calculates the average of the numbers in a given list.
# Note: Empty arrays should return 0.

def find_average(numbers):
    if not numbers:
        return 0
    else:
        num = sum(numbers) / len(numbers)
        return num

assert find_average([1, 2, 3]) == 2
assert find_average([]) == 0
assert find_average([1, 2]) == 1.5
print("OK")