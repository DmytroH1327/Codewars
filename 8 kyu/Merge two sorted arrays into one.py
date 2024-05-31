

def merge_arrays(arr1, arr2):
    num = sorted(arr1 + arr2)
    numbers_unique = list(dict.fromkeys(num))
    return numbers_unique


assert merge_arrays([1,2,3,4], [5,6,7,8]) == [1,2,3,4,5,6,7,8]
assert merge_arrays([1,3,5,7,9], [10,8,6,4,2]) == [1,2,3,4,5,6,7,8,9,10]
assert merge_arrays([1,3,5,7,9,11,12], [1,2,3,4,5,10,12]) == [1,2,3,4,5,7,9,10,11,12]
print("OK")