# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
# Example: (Input1, Input2 -->Output)
# "4",  "5" --> "9"
# "34", "5" --> "39"
# "", "" --> "0"
# "2", "" --> "2"
# "-5", "3" --> "-2"

def sum_str(a, b):
    if not a and not b:
        return "0"
    elif not a:
        return b
    elif not b:
        return a
    else:
        return str(int(a) + int(b))

assert sum_str("4", "5") == "9"
assert sum_str("34", "5") == "39"
assert sum_str("9", "") == "9"
assert sum_str("", "9") == "9"
assert sum_str("", "") == "0"
print("OK")