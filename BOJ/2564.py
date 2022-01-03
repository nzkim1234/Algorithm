from sys import stdin

y, x = map(int,stdin.readline().split())
n = int(stdin.readline())
position = []

# 입력 받은 값에 따른 좌표를 position에 추가
for _ in range(n + 1):
    direction, distance = map(int, stdin.readline().split())

    if direction == 1:
        position.append([0, distance])
    elif direction == 2:
        position.append([x, distance])
    elif direction == 3:
        position.append([distance, 0])
    else:
        position.append([distance, y])

my_position_x, my_position_y = position.pop()  # 마지막 값은 나의 좌표이므로 position에 pop
result = 0

for p_x, p_y in position:
    calc_distance_x = p_x - my_position_x
    calc_distance_y = p_y - my_position_y

    if abs(calc_distance_x) == x:  # 상점과 나의 위치가 위 아래로 양 끝 일때
        result += x + min(p_y + my_position_y, y * 2 - my_position_y - p_y)  # x + 반시계 또는 시계 방향으로 돌았을 때 최솟값
    elif abs(calc_distance_y) == y: # 상점과 나의 위치가 좌 우로 양 끝 일때
        result += y + min(p_x + my_position_x, x * 2 - my_position_x - p_x)  # y + 반시계 또는 시계 방향으로 돌았을 때 최솟값
    else:
        result += abs(calc_distance_x) + abs(calc_distance_y)  

print(result)