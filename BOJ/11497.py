from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    graph = sorted(list(map(int, stdin.readline().split())), reverse=True)  # 내림차순으로 정리
    result = 0

    for i in range(n - 2):
        result = max(result, graph[i] - graph[i + 2])  # 자신의 인덱스 값 - 자신의 인덱스 + 2 한 인덱스의 값 의 최댓값이 결과값
    
    print(result)
