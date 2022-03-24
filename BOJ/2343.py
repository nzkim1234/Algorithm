from sys import stdin

n, m = map(int, stdin.readline().split())
graph = list(map(int,stdin.readline().split()))
end = sum(graph)
start = min(graph)

while start <= end:
    mid = (start + end) // 2
    count = 0
    current_sum = graph[0]
    
    for i in range(1, n):
        if current_sum + graph[i] > mid:
            count += 1
            current_sum = graph[i]
        else:
            current_sum += graph[i]


    print(start, end, mid, count)
    if count >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)