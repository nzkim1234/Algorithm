from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    turtle = [0, 0]  # 거북이 첫 위치
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 이동 가능한 위치
    index = 0

    # X축의 최댓값, 최솟값
    max_x = 0
    min_x = 0
    
    # Y축의 최댓값, 최솟값
    max_y = 0
    min_y = 0

    # 입력받기
    command = list(map(str,stdin.readline().strip()))
    
    for i in command:
        # 앞으로 갈 경우 규칙에 맞을 시 x,y의 좌표를 갱신
        if i == 'F':
            turtle[0] += direction[index][0]
            turtle[1] += direction[index][1]
            max_x = max(max_x, turtle[0])
            max_y = max(max_y, turtle[1])
            min_x = min(min_x, turtle[0])
            min_y = min(min_y, turtle[1])
        
        # 뒤로 갈 경우 규칙에 맞을 시 x,y의 좌표를 갱신
        elif i == 'B':
            turtle[0] -= direction[index][0]
            turtle[1] -= direction[index][1]
            max_x = max(max_x, turtle[0])
            max_y = max(max_y, turtle[1])
            min_x = min(min_x, turtle[0])
            min_y = min(min_y, turtle[1])

        # 방향 전환
        elif i == 'L':  
            index -= 1
            if index < 0:
                index = 3
        
        # 방향 전환
        else:
            index += 1
            if index > 3:
                index = 0

    print((max_x - min_x) * (max_y - min_y))