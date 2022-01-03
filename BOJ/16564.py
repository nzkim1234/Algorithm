n, k = map(int, input().split())
x = []
if n == 1:
    print(n+k)
    quit()
for _ in range(n):
    x.append(int(input()))
start = min(x)
end = max(x)
if k == 0:
    print(start)
    quit()
while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in range(n):
        if x[i] < mid:
            count += mid - x[i]
    if count <= k:
        start = mid + 1
    else:
        end = mid - 1
print(end)
