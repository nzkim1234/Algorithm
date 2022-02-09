from audioop import reverse
from sys import stdin

s = list(map(str, stdin.readline().strip()))
result = []
opened = False
stack = []
for a in s:
    if a == '<':
        opened = True
        stack.reverse()
        result += stack
        result.append(a)

        stack = []
    elif a == '>':
        opened = False
        result.append(a)
    else:
        if opened:
            result.append(a)
        else:
            if a == ' ':
                stack.reverse()
                result += stack
                stack = []
                result.append(a)
            else:
                stack.append(a)
stack.reverse()
result += stack
for i in result:
    print(i, end = '');