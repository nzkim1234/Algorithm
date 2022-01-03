t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    priority = []
    for i in range(n): # 중요도, 순서을 저장
        priority.append([l[i],i])
    c = 0
    while True:
        result = 'IMPOSSIBLE_VALUE' # 초기값
        if max(priority, key = lambda x : x[0]) == priority[0]: # 현재 첫번쨰 순서의 중요도가 최댓값일 경우 result에 저장
            result = priority.pop(0)
            c += 1
        else: # 아닐시 제일 뒤로 보냄
            priority.append(priority.pop(0))
        if result[1] == m: # result의 순번이 m 일때 결과 출력
            print(c)
            break