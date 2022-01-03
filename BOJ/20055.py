from collections import deque
n, k = map(int,input().split())
a = list(map(int, input().split()))
conveyor_belt = deque()
for i in a:
    conveyor_belt.append([i,False])
count = 0
while k > 0 :
    count += 1
    conveyor_belt.appendleft(conveyor_belt.pop())
    if conveyor_belt[n-1][1] == True:
        conveyor_belt[n-1][1] = False
    for i in range(n-2, -1, -1):
        if conveyor_belt[i][1] == True:
            if conveyor_belt[i+1][1] == False and conveyor_belt[i+1][0] > 0:
                conveyor_belt[i][1] = False
                conveyor_belt[i+1][0] -= 1
                if conveyor_belt[i+1][0] == 0:
                    k -= 1
                conveyor_belt[i+1][1] = True
    if conveyor_belt[n-1][1] == True:
        conveyor_belt[n-1][1] = False
    if conveyor_belt[0][0] > 0:
        conveyor_belt[0][1] = True
        conveyor_belt[0][0] -= 1
        if conveyor_belt[0][0] == 0:
                    k -= 1
print(count)
