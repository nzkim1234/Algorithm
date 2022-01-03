import sys
input = sys.stdin.readline
n = int(input())
point = []
for i in range(n):
    x, y = map(int, input().split())
    point.append([x,y])
point.sort()
for i in point:
    print(i[0], i[1])

"""
n = int(input())
point = []
for i in range(n):
    x, y = map(int, input().split())
    point.append([x,y])
point.sort(key = lambda x:(x[0], x[1]))
for i in point:
    print(i[0], i[1])

"""