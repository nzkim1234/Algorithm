from sys import stdin
import heapq

n = int(stdin.readline())
heap = []

for _ in range(n):
    x = int(stdin.readline())
    
    if x == 0:
        if heap:
            a, b = heapq.heappop(heap)
            print(a * b)
        else:
            print(x)
    
    else:
        if x < 0:
            heapq.heappush(heap, [-x, -1])
        else:
            heapq.heappush(heap, [x, 1])