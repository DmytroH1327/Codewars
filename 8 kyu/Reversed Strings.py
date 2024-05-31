# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def solution(string):
    return string[::-1]


assert solution('world') == 'dlrow'
assert solution('hello') == 'olleh'
assert solution('') == ''
assert solution('h') == 'h'
print("OK")