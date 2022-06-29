from sys import stdin
import heapq

n = int(stdin.readline())
heap = []

for _ in range(n):
    x = int(stdin.readline())
    
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(x)
    
    else:
        heapq.heappush(heap, -x)