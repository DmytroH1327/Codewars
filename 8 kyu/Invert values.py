def invert(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i * -1)
    return new_lst

assert invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
assert invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
assert invert([]) == []
print("OK")