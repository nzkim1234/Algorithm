from sys import stdin
from itertools import combinations

n = int(stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))
    
teams = list(combinations([i for i in range(n)], n//2))  # 나올 수 있는 모든 조합 찾기
start_team = teams[0:len(teams)//2]  # 조합의 앞에서부터 절반 저장
link_team = list(reversed(teams[len(teams)//2 ::]))  # 조합의 뒤에서부터 절반을 뒤집어서 저장

result = 1e9

for i in range(len(start_team)):
    start_ability = 0
    link_ability = 0

    # 팀에서 2명씩 짝을 지어서 계산한 값을 저장
    for x, y in combinations(start_team[i], 2):
        start_ability += graph[x][y] + graph[y][x]
    
    # 팀에서 2명씩 짝을 지어서 계산한 값을 저장
    for x, y in combinations(link_team[i], 2):
        link_ability += graph[x][y] + graph[y][x]
    
    # 두 팀의 차이가 제일 적은 값을 result에 저장
    result = min(result, abs(start_ability - link_ability))

print(result)
