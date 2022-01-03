from collections import deque
n = int(input())
arr = deque(i+1 for i in range(n))
count = 0
while len(arr) != 1:
    if count % 2 == 0:
        card = arr.popleft()
    else:
        card = arr.popleft()
        arr.append(card)
    count += 1
print(arr[0])
