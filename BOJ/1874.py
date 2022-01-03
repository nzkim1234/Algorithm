n = int(input())
a = sorted([int(i) for i in range(n+1)], reverse=True)
arr = []
result = []
for _ in range(n):
    arr.append(int(input()))
stack = [a.pop(-1), a.pop(-1)]
result.append('+')
for i in arr:
    while True:
        if stack[-1] == i:
            result.append('-')
            stack.pop(-1)
            break
        if len(a) != 0:
            stack.append(a.pop(-1))
            result.append('+')
        else:
            print('NO')
            quit()
for i in result:
    print(i)
