from sys import stdin

n, m = map(int, stdin.readline().split())
time_list = []

for _ in range(n):
    time_list.append(int(stdin.readline()))
start = 0
end = int(1e9) * m

while start < end:
    mid = (start + end) // 2
    total = 0

    for i in time_list:
        total += mid // i
    
    if total >= m:
        end = mid 
    else:
        start = mid + 1

print(end)