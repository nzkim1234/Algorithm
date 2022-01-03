n = int(input())
p = list(map(int,input().split()))
line = [0 for _ in range(n)] # 줄 생성
c = 1
for i in p:
    for j in range(n): # n만큼 반복
        if i == 0: # i(왼쪽에 있는 사람 수)r가 0 일 때
            if line[j] == 0: # 칸이 비어있으면 사람 할당
                line[j] = c
                break
        if line[j] == 0: # 칸이 비어있을시 i(왼쪽에 있는 사람 수) 감소
            i -= 1
    c += 1
print(*line)
