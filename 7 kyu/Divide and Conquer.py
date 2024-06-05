# Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.
# Return as a number.

def div_con(x):
    num_lst = []
    str_lst = []
    for i in x:
        if isinstance(i, int):
            num_lst.append(i)
        elif isinstance(i, str):
            str_lst.append(int(i))

    num = (sum(num_lst) - sum(str_lst))
    return num

assert div_con([9, 3, '7', '3']) == 2
assert div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]) == 14
assert div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']) == 13
assert div_con(['1', '5', '8', 8, 9, 9, 2, '3']) == 11
assert div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]) == 61
print("OK")