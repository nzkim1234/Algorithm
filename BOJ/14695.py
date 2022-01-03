n = int(input())
h = list(map(int, input().split()))
count = 0
result = 0
a = h[0]
for i in h:
    if a > i:
        count += 1
    else:
        a = i
        result = max(result, count)
        count = 0
result = max(result, count)
print(result)
