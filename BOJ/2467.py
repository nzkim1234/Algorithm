from sys import stdin

n = int(stdin.readline())
graph = list(map(int, stdin.readline().split()))
graph.sort()  # 오름차순 정렬이기 떄문에 sort()할 필요는 없다
start = 0
end = len(graph) - 1
result = [abs(graph[start] + graph[end]), graph[start], graph[end]]

while start < end:
    add = graph[start] + graph[end]  # 두 용액의 합
    
    # 용액의 절댓값이 기존 결과보다 작으면 갱신
    if abs(add) < result[0]:
        result = [abs(add), graph[start], graph[end]]

    if add > 0:  # 합이 양수면 오른쪽을 -1
        end -= 1   
    elif add < 0:  # 합이 음수면 왼쪽을 +1
        start += 1
    else:  # 합이 0이면 break
        break

print(result[1], result[2])
