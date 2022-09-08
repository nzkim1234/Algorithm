def solution(n, k):
    answer = 0
    change = ""

    while n != 0:
        change += str(n % k)
        n = n // k

    change = "".join(list(reversed(change))).split('0')
    graph = [True] * 1000001
    graph[0], graph[1] = False, False
    
    for i in range(2, 1000001):
        if graph[i]:
            for j in range(i + i, 1000001, i):
                graph[j] = False

    for i in change:
            if i and graph[int(i)]:
                answer += 1
    
    return answer