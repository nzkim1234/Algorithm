from sys import stdin

n, m = map(int, stdin.readline().split())  # 입력받기

graph = []

# 입력받기
for _ in range(n):
    graph.append(list(map(str, stdin.readline().strip())))

min_change_b, min_change_w = 1e9, 1e9  # 최종결과2종
color = ['W', 'B']  # 칸의 색 판단

for i in range(n):
    # 범위 벗어났을 시
    if i + 7 >= n:
        break
    
    for j in range(m):
        # 범위 벗어났을 시
        if j + 7 >= m:
            break
        
        change_to_b, change_to_w = 0, 0  # 결과값 저장
        count = 0  # 칸 수에 따른 값 찾기위한 변수

        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if graph[x][y] == color[count % 2]:
                    change_to_b += 1

                if graph[x][y] == color[(count + 1) % 2]:
                    change_to_w += 1
                
                count += 1
            
            count += 1

        min_change_b = min(min_change_b, change_to_b)  # 갱신
        min_change_w = min(min_change_w, change_to_w)  # 갱신

print(min(min_change_b, min_change_w))