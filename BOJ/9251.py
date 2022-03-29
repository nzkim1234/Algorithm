from sys import stdin

line = list(map(str,stdin.readline().strip()))
line2 = list(map(str,stdin.readline().strip()))

graph = [[0 for _ in range(len(line) + 1)] for _ in range(len(line2) + 1)]  # 2차원 배열 생성

for x in range(1, len(line2) + 1):
    for y in range(1, len(line) + 1):
        if line2[x - 1] == line[y - 1]:  # 값이 같다면 위치에서 [-1, -1] 위치에 값 +1
            graph[x][y] = graph[x-1][y-1] + 1
        else:  # 다르다면 자신의 이전값 또는 자신의 -1열 의 값 중 최대값 가져오기
            graph[x][y] = max(graph[x][y - 1], graph[x - 1][y])

        # print(line2[x - 1], line[y - 1])
        # for k in graph:
        #     print(k)
        # print()

print(graph[-1][-1])
