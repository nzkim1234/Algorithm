from sys import stdin

n = int(stdin.readline())

len_s = int(stdin.readline())
s = list(map(str, stdin.readline()))
p = ['I', 'O', 'I']

len_p = len(p)
count = 0

i = 0
count = 0
result = 0

while i < len_s - 1:
    if s[i : i + len_p] == p:
        i += 2
        count += 1
        if count == n:
            result += 1
            count -= 1
    else:
        i += 1
        count = 0

print(result)