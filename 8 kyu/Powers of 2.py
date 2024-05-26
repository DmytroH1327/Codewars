# Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

def powers_of_two(n):
    n_lst = []
    for i in range(n + 1):
        n_lst.append(2 ** i)
    return n_lst

assert powers_of_two(0) == [1]
assert powers_of_two(1) == [1, 2]
assert powers_of_two(4) == [1, 2, 4, 8, 16]
print("OK")
