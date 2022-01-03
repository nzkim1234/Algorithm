n, m = map(int, input().split())
house = []
chicken_house = []
for i in range(n): # graph를 입력받고 house, chicken_house의 좌표만 가져오기
    graph = list(map(int, input().split()))
    for j in range(n):
        if graph[j] == 1:
            house.append([i+1, j+1])
        elif graph[j] == 2:
            chicken_house.append([i+1, j+1])
c_h = []
for i in range(1<<len(chicken_house)): # chicken_house의 부분집합 구하기
    r = []
    for j in range(len(chicken_house)):
        if i & (1 << j):
            r.append(chicken_house[j])
    if len(r) == m: # 부분 집합의 원소의 갯수가 m이랑 같을때만 c_h에 추가
        c_h.append(r)
t_r = []
for i in c_h:
    c_r = 0
    for h_x, h_y in house:
        h_r = n*n
        for c_x, c_y in i:
            h_r = min(h_r, abs(h_x-c_x) + abs(h_y-c_y))
        c_r += h_r
    t_r.append(c_r)
print(min(t_r))
