n = int(input())
for i in range(n):
    stack = []
    line = input()
    for i in line:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']' or i == ')':
            if len(stack) != 0:
                if i == ']':
                    if stack[-1] == '[':
                        stack.pop()
                elif i == ')':
                    if stack[-1] == '(':
                        stack.pop()
            else:
                stack.append(i)
                break

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
