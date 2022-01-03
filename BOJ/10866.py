import sys
from collections import deque
input = sys.stdin.readline
a = deque()
n = int(input())

for i in range(n):
    order = input().split()
    if order[0] == "push_back":
        a.append(int(order[1]))
    elif order[0] == "push_front":
        a.appendleft(int(order[1]))
    elif order[0] == "pop_front":
        if len(a) != 0:
            print(a.popleft())
        else:
            print(-1)
    elif order[0] == "pop_back":
        if len(a) != 0:
            print(a.pop())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(a))
    elif order[0] == "empty":
        if len(a) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if len(a) != 0:
            print(a[0])
        else:
            print(-1)
    elif order[0] == "back":
        if len(a) != 0:
            print(a[-1])
        else:
            print(-1)
