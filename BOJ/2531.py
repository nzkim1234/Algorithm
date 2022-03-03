from sys import stdin
from collections import deque

n, d, k, c = map(int, stdin.readline().split())
line = []

for _ in range(n):
    line.append(int(stdin.readline()))

start = 0  # 초밥을 먹기 시작할 인덱스
result = 0

while True:
    end = start + k  # 초밥 먹기를 끝낼 인덱스를 표시
    can_eat = []
    count = 0  # 먹은 초밥의 갯수 

    if start > n - 1:  # 먹기 시작하는 초밥이 리스트를 벗어나면 break
        break
    
    if end > n - 1:  # end의 인덱스 값이 초밥의 길이보다 커질때
        end = end % n

    # 초밥 먹기
    for i in range(k):
        index = start + i

        if index > n - 1:
            break
        
        can_eat.append(line[start + i])
        count += 1
    
    # 먹은 갯수가 부족하다면 더 먹어주기
    if count < k:
        can_eat += line[:end]
    
    # 먹은 초밥중 c가 없으면 추가해주기
    if not c in can_eat:
        can_eat.append(c)

    result = max(result, len(set(can_eat)))  # set로 중복을 제거한 뒤, 총 먹은 종류 파악, max값 구하기
    start += 1

print(result)
