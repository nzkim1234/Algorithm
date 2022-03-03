from sys import stdin
from collections import deque

n = int(stdin.readline())
input = list(map(int, stdin.readline().split()))
graph = deque()

for i in range(n):
    graph.append([i + 1, input[i]])

rotate = 0  # 이동할 횟수 표시할 변수
result = []

while graph:
    if rotate == 0:  # 이동 횟수가 0이면 새로운 풍선을 터트려야한다.
        value = graph.popleft()  # 터트릴 풍선의 값 가져오기
        result.append(value[0])  # 터트릴 풍선의 번호 저장
        
        # 이동횟수를 판단하여 rotate 갱신
        if value[1] < 0:
            rotate = value[1] 
        else:
            rotate = value[1] - 1
    
    if not graph:  # 덱이 비어있으면 break
        break
    
    if rotate < 0:  # 이동방향이 왼 -> 오 일 때, rotate가 음수 일 때
        rotate += 1
        graph.appendleft(graph.pop())
    else:  # 이동방향이 오 -> 왼 일 때, rotate가 양수 일 때
        rotate -= 1
        graph.append(graph.popleft())

print(*result)
