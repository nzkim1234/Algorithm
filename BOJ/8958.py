t = int(input())
for _ in range(t):
    n = input()
    count = 0
    result = 0
    for i in range(len(n)):
        if n[i] == 'O':
            count += 1
            result += count
        else:
            count = 0
    print(result)
