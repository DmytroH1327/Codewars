# Find the difference between the sum of the squares of the first n natural numbers (1 <= n <= 100) and the square of their sum.


def difference_of_squares(n):
    number_squares = []
    number_lst = list(range(1, n + 1))
    number_sum = sum(number_lst) ** 2

    for number in number_lst:
        number_squares.append(number ** 2)

    return number_sum - sum(number_squares)


assert difference_of_squares(5) == 170
assert difference_of_squares(10) == 2640
assert difference_of_squares(100) == 25164150
print("OK")
