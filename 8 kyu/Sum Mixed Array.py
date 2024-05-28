# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
#
# Return your answer as a number.

def sum_mix(arr):
    number = []
    for num in arr:
        number.append(int(num))
    return sum(number)

assert sum_mix([9, 3, '7', '3']) == 22
assert sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]) == 42
assert sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']) == 41
assert sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']) == 45
assert sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]) == 61
print("OK")