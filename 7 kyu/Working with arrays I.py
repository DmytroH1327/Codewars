# In this kata the function returns an array/list of numbers without its last element. The function is already written for you and the basic tests pass, but random tests fail. Your task is to figure out why and fix it.
# Good luck!
# Hint: watch out for side effects.

def without_last(lst):
    return lst[:-1]


assert without_last([1, 2, 3, 4, 5]) == [1, 2, 3, 4]
assert without_last([9, 7, 6, 9]) == [9, 7, 6]
assert without_last([9, 97, 88, 38]) == [9, 97, 88]
assert without_last([6, 35, 81, 51, 54, 24, 25, 76]) == [6, 35, 81, 51, 54, 24, 25]
assert without_last([81, 72, 86, 21, 44, 19, 98, 81, 37]) == [81, 72, 86, 21, 44, 19, 98, 81]
print("OK")