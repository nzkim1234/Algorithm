t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = []
    for i in range(n):
        queue.append([arr[i], i+1])
    count = 0
    while True:
        p, loc = queue.pop(0)
        if len(queue) == 0:
            print(count+1)
            break
        if p >= max(queue)[0]:
            count += 1
            if loc == m+1:
                print(count)
                break
        else:
            queue.append([p, loc])
