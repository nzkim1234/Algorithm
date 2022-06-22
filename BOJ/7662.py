from sys import stdin
import heapq

t = int(stdin.readline())

for _ in range(t):
    k = int(stdin.readline())
    min_heap, max_heap = [], []
    visited = [False] * k

    for i in range(k):
        alpha, num = stdin.readline().split()

        if alpha == 'I':
            heapq.heappush(min_heap, (int(num), i))
            heapq.heappush(max_heap, (-int(num), i))
            visited[i] = True

        else:
            if num == '1':
                # 두개의 힙 맞춰주기
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                
                # 해당하는 원소 삭제
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            
            else:
                # 두개의 힙 맞춰주기
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                # 해당하는 원소 삭제
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    # 두개의 힙 맞춰주기
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    # 두개의 힙 맞춰주기
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
        
    else:
        print(-max_heap[0][0], min_heap[0][0])

        