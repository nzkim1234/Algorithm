import sys
input = sys.stdin.readline

n, m = map(int ,input().split())
t = []
for _ in range(n):
    t.append(int(input()))
s = 1
e = max(t) * m
while s < e:
    mid = (s+e)//2
    pass_p = 0
    for i in t:
        pass_p += mid//i
    if pass_p >= m:
        e = mid
    else:
        s = mid + 1
print(e)
