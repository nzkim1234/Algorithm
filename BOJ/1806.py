from sys import stdin

n ,s = map(int ,stdin.readline().split())

queue = list(map(int, stdin.readline().split()))

start = end = 0
current_sum = 0
result_len = 1e9

while start <= end:
    if current_sum >= s:
        result_len = min(result_len, end - start)
        current_sum -= queue[start]
        start += 1
    elif end == n:
        break
    else:
        current_sum += queue[end]
        end += 1
        
if result_len == 1e9:
    print(0)
else:
    print(result_len )