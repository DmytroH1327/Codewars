# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". 
# Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    n_str = ""
    if n == 0:
        return n_str
    else:
        for i in range(1, n + 1):
            n_str += str(i) + " sheep..."
        return n_str


assert count_sheep(0) == ""
assert count_sheep(1) == "1 sheep..."
assert count_sheep(2) == "1 sheep...2 sheep..."
assert count_sheep(3) == "1 sheep...2 sheep...3 sheep..."
print("OK")
