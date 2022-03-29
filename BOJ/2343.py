from sys import stdin

n, m= map(int, stdin.readline().split())
graph = list(map(int, stdin.readline().split()))

start = max(graph)
end = sum(graph)
result = 1e9

while start <= end:
    mid = (start + end) // 2

    count = 0
    current_range = 0
    # 리스트를 돌면서 강의 영상의 길이 확인
    for i in range(n):
        if current_range + graph[i] <= mid:  # 중간값보다 작을 시 한편의 강의에 추가
            current_range += graph[i]
        else:  # 중간값보다 클 시 새로운 한편의 강의 추가 
            current_range = graph[i] 
            count += 1

    # 강의의 영상이 많으면 start 증가, 적으면 end 감소
    if count <= m - 1:
        end = mid - 1
        result = min(result, mid)
    else:
        start = mid + 1

print(result)
