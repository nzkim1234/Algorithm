from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[] for _ in range(n)]
x, y = 0, 0
result = []

# x, y가 -1, -1이 아닐 때까지 입력받기
while x + y >= 0:
    x, y = map(int,stdin.readline().split())

    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

# 자신의 친구를 저장하는 리스트 생성
for i in range(n):
    score = 1
    do_know = [False for i in range(n)]  # 총 회원의 수만큼 False로 할당
    do_know[i] = True  # 자기 자신을 True로 변경
    queue = deque()

    # 자기 자신과 친구인 회원을 조사
    for j in graph[i]:  
        if not do_know[j]:
            queue.append(j)  # 자신과 친구인 회원을 queue에 저장
            do_know[j] = True  # 자신과 친구인 회원의 번호를 True로 변경

    # 모든 회원과 친구일 경우 score를 result에 저장 후 continue
    if not False in do_know:
        result.append(score)
        continue
    
    
    queue.append(-1)  # 저장해뒀던 queue를 알기 위한 -1 
    score += 1
    
    while queue:
        num = queue.popleft()

        # 저장해뒀던 queue를 다 돌았을 때
        if num == -1:
            #  모든 회원과 친구일 경우 score를 result에 저장 후 break
            if not False in do_know:
                result.append(score)
                break
            
            # 아닐 경우 
            score += 1
            queue.append(-1)
            continue
        
        # 친구인 회원을 조사
        for j in graph[num]:
            if not do_know[j]:
                queue.append(j)
                do_know[j] = True
                
candidate = []

for i in range(n):
    # result[i]의 값이 result의 최솟값과 같을경우
    if result[i] == min(result):
        candidate.append(i + 1)

print(min(result), len(candidate))
print(*candidate)
