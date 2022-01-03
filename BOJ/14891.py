from sys import stdin
from collections import deque

gear = deque()
queue = deque()
move = []

for _ in range(4):
    gear.append(deque(stdin.readline().strip()))

k = int(stdin.readline())

for _ in range(k):
    visit_gear = [0, 0, 0, 0]  # 4개의 기어를 각각 방문했는지 확인하기 위한 리스트
    moving_gear, direction = map(int,stdin.readline().split())
    moving_gear -= 1
    visit_gear[moving_gear] = 1
    queue.append([moving_gear, direction])

    while queue:
        moving_gear, direction = queue.popleft()
        
        # 기어의 오른편에 기어가 있고, 맞닿은 극이 서로 다를 시
        if moving_gear + 1 < 4 and gear[moving_gear][2] != gear[moving_gear + 1][-2] and not visit_gear[moving_gear + 1]:
            visit_gear[moving_gear + 1] = 1  # 오른편기어를 방문표시
            queue.append([moving_gear + 1, -direction])  # 큐에 저장, (바로 옆에있는 기어는 자신과 반드시 반대방향으로 돈다.)

        # 기어의 왼편에 기어가 있고, 맞닿은 극이 서로 다를 시
        if moving_gear - 1 >= 0 and gear[moving_gear][-2] != gear[moving_gear - 1][2] and not visit_gear[moving_gear - 1]:
            visit_gear[moving_gear - 1] = 1  # 왼편기어를 방문표시
            queue.append([moving_gear - 1, -direction])  # 큐에 저장, (바로 옆에있는 기어는 자신과 반드시 반대방향으로 돈다.)
            
        if direction > 0:  # 시계 방향 회전
            gear[moving_gear].appendleft(gear[moving_gear].pop())
        else:  # 빈시계 방향 회전
            gear[moving_gear].append(gear[moving_gear].popleft())

result = 0

# 결과 계산
for i in range(len(gear)):
    if gear[i][0] == '1':
        result += 2 ** i

print(result)
