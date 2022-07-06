from sys import stdin

n = int(stdin.readline())
graph = list(map(int, stdin.readline().split()))
set_graph = sorted(set(graph))  # 중복 제거, 정렬
dic = dict()

# 순서 부여
for i in range(len(set_graph)):
    dic[set_graph[i]] = i

# 좌표 압축
for i in graph:
    print(dic[i], end = ' ')
