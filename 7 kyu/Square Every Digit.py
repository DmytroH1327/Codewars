# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

def square_digits(num):
    number = ""
    for i in str(num):
        number += str(int(i) ** 2)
    return int(number)


assert square_digits(9119) == 811181
assert square_digits(0) == 0
print("OK")