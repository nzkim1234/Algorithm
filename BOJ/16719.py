from sys import stdin
 
word = list(stdin.readline().strip())
result = [''] * len(word)
 
def func(string, start):
    if not string:
        return

    _min = min(string)
    index = string.index(_min)
    result[start + index] = _min

    print("".join(result))

    func(string[index + 1:], start + index + 1)
    func(string[:index], start)
 
 
func(word, 0)