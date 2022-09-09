from collections import deque


def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    total = (sum_1 + sum_2) // 2
    count = 0

    while True:
        if not (queue1 and queue2):
            count = -1

            break
        
        if sum_1 == total:
            break
        elif sum_1 > total:
            sum_1 -= queue1.popleft()
        else:
            queue1.append(queue2.popleft())
            sum_1 += queue1[-1]
            
        count += 1
        
    return count
    

solution([3, 2, 7, 2], [4, 6, 5, 1])
solution([1, 1], [1, 5])
