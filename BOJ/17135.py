from sys import stdin
from itertools import combinations
from copy import deepcopy

n, m, d = map(int, stdin.readline().split())
graph = [stdin.readline().strip().split() for _ in range(n)]
archer_locations = list(combinations([i for i in range(m)], 3))  # 궁수가 배치될 수 있느 모든 경우의 수
result = 0

for i in archer_locations:
    count = 0
    new_graph = deepcopy(graph)

    while new_graph:
        len_new_graph = len(new_graph)
        total_remove_loc = []

        for archer_loc in i:
            remove_loc = []     

            #그래프의 아래에서부터 사정거리(d)까지에서 적의 위치, 궁수로부터의 거리 찾기
            for find_enemy_x in range(1, d + 1):
                find_enemy_x = len_new_graph - find_enemy_x

                for find_enemy_y in range(m):
                    if find_enemy_x >= 0 and new_graph[find_enemy_x][find_enemy_y] == '1':
                            distance = abs(len_new_graph - find_enemy_x) + abs(find_enemy_y - archer_loc)
                            
                            if distance <= d:  #적으로부터 거리가 d 이하라면 remove_loc에 저장
                                remove_loc.append([find_enemy_x, find_enemy_y, distance])

            if remove_loc:
                remove_loc.sort(key = lambda x : (x[2], x[1]))  # 적을 거리, 위치(가장 왼쪽 왼쪽) 순으로 정렬
                total_remove_loc.append(remove_loc[0])  # 이 궁수가 제거할 적의 위치(remove_loc[0])을 total_remove_loc에 저장

        # 각 궁수가 제거할 적을 제거 후 제거한 적의 수만큼 count 증가
        for x, y, no_use in total_remove_loc:
            if new_graph[x][y] == '1':
                new_graph[x][y] = '0'
                count += 1

        del(new_graph[len_new_graph - 1])  # 그래프의 마지막 행 삭제

    result = max(result, count)  # 각 경우의 수에서 count의 최대값을 구하기

print(result)
