# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
# Examples:
# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"

def get_middle(s):
    mid_index = len(s) // 2
    if len(s) % 2 == 0:
        first_a = s[:mid_index]
        second_b = s[mid_index:]
        return first_a[-1] + second_b[0]
    else:
        return s[mid_index]


assert get_middle("test") == "es"
assert get_middle("testing") == "t"
assert get_middle("middle") == "dd"
assert get_middle("A") == "A"
assert get_middle("of") == "of"
print("OK")