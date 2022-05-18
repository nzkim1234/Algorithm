from sys import stdin

n = int(stdin.readline())
result = [1]*n
graph = [[] for _ in range(n)]  # 노드의 연결 저장
graph2=[]  # 전체 정보 저장
visited = {}

def gcd(x, y):
    while y:
        x, y = y, x % y
    
    return x

# 비율을 통일 시켜주는 함수
def change(a, p, d):
    global visited

    if not (a, p) in visited:
        visited[(a, p)] = True
        result[a] *= p
    
        for i in graph[a]:
            if i != d: 
                change(i, p, a)

# 입력 받기
for _ in range(n-1):
    a, b, p, q = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph2.append([a, b, p, q])

for i in range(n-1):
    a, b, p, q = graph2[i]
    visited={}

    change(a, p, b)
    change(b, q, a)

base = result[0]

# 최대 공약수 구하기
for i in range(n):
    base = gcd(base, result[i])

# 구한 최대 공약수로 나눠줘서 결과 구하기
for i in range(n): 
    result[i] = result[i] // base

print(*result)
