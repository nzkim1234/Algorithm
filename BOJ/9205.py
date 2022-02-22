from sys import stdin
from collections import deque

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())  # 입력받을 편의점 수
    beer = 20  # 맥주 기본값
    home = list(map(int, stdin.readline().split()))  # 집 좌표
    cvs = []  # 편의점 좌표

    for _ in range(n):
        cvs.append(list(map(int, stdin.readline().split())))

    end = list(map(int, stdin.readline().split()))  # 목적지 좌표
    location = cvs + [end]  # 모든 좌표 합치기 (집 제외)
    queue = deque([[home[0], home[1], beer]])  # 덱 생성
    visit = [queue[0]]  # 방문한 좌표 생성
    success = False  # 성공 표시

    # bfs 탐색
    while queue:
        x, y, beer = queue.popleft()

        # 목적지에 도착했으면 success 참으로
        if [x, y] == end:
            success = True
            break
        
        # 방문에 의미가 있는 좌표를 돌면서 현재 위치에서 도달 가능한지 탐색, 도달가능하면 덱에 추가
        for n_x, n_y in location:
            if [n_x, n_y, 20] not in visit:
                length = abs(n_x - x) + abs(n_y - y)

                if beer * 50 >= length:
                    queue.append([n_x, n_y, 20])
                    visit.append([n_x, n_y, 20])
    
    # 결과 출력
    if success:
        print('happy')
    else:
        print('sad')
