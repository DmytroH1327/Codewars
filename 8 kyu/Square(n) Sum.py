# Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    num = []
    for number in numbers:
        num.append(number**2)
    return sum(num)

assert square_sum([1, 2]) == 5
assert square_sum([0, 3, 4, 5]) == 50
assert square_sum([]) == 0
assert square_sum([-1, -2]) == 5
assert square_sum([-1, 0, 1]) == 2
print("OK")