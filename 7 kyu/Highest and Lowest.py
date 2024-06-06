# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

def high_and_low(numbers):
    number_list = []
    num = numbers.split()
    for i in num:
        number_list.append(int(i))
    max_num = max(number_list)
    min_num = min(number_list)
    return f"{max_num} {min_num}"


assert high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4") == "42 -9"
assert high_and_low("1 2 3") == "3 1"
print("OK")