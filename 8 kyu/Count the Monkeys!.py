# You take your son to the forest to see the monkeys. You know that there are a certain number there (n), but your son is too young to just appreciate the full number, he has to start counting them from 1.
# As a good parent, you will sit and count with him. Given the number (n), populate an array with all numbers up to and including that number, but excluding zero.

def monkey_count(n):
    num = list(range(1, n+1))
    return num

assert monkey_count(5) == [1, 2, 3, 4, 5]
assert monkey_count(3) == [1, 2, 3]
assert monkey_count(9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert monkey_count(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert monkey_count(20) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("OK")