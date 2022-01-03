import sys
input = sys.stdin.readline
m = int(input())

s = []

for i in range(m):
    order = input().strip().split()
    if order[0] == 'add':
        if not int(order[1]) in s:
            s.append(int(order[1]))
    elif order[0] == 'remove':
        if int(order[1]) in s:
            s.remove(int(order[1]))
    elif order[0] == 'check':
        if int(order[1]) in s:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if int(order[1]) in s:
            s.remove(int(order[1]))
        else:
            s.append(int(order[1]))
    elif order[0] == 'all':
        s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
             15, 16, 17, 18, 19, 20]
    elif order[0] == 'empty':
        s = []
