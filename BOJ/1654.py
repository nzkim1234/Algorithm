n, k = map(int, input().split())
cable = []
for _ in range(n):
    cable.append(int(input()))
start = 1
end = max(cable)
while start <= end:
    mid = (start+end) // 2
    count = 0
    for i in cable:
        count += i // mid
    if count >= k:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
