# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    text = s.split()
    num_len = []
    count = 0
    for i in text:
        num_len.append(len(i))
    return min(num_len)


assert find_short("bitcoin take over the world maybe who knows perhaps") == 3
assert find_short("turns out random test cases are easier than writing out basic ones") == 3
assert find_short("lets talk about javascript the best language") == 3
assert find_short("i want to travel the world writing code one day") == 1
assert find_short("Lets all go on holiday somewhere very cold") == 2
assert find_short("Let's travel abroad shall we") == 2
print("OK")