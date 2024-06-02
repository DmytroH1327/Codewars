# Create a function that always returns True/true for every item in a given list.
# However, if an element is the word 'flick', switch to always returning the opposite boolean value.

def flick_switch(lst):
    bool_lst = []
    result = True
    for i in lst:
        if i == 'flick':
            result = not result
        bool_lst.append(result)
    return bool_lst


assert flick_switch(['codewars', 'flick', 'code', 'wars']) == [True, False, False, False]
assert flick_switch(['flick', 'chocolate', 'adventure', 'sunshine']) == [False, False, False, False]
assert flick_switch(['bicycle', 'jarmony', 'flick', 'sheep', 'flick']) == [True, True, False, False, True]
assert flick_switch(['bicycle']) == [True]
assert flick_switch(['john, smith, susan', 'flick']) == [True, False]
assert flick_switch(['flick', 'flick', 'flick', 'flick', 'flick']), [False, True, False, True, False]
assert flick_switch([]) == []
print("OK")