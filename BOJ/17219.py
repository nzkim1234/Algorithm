from sys import stdin

n, m = map(int, stdin.readline().split())

dic = dict()

for _ in range(n):
    site, pw = stdin.readline().strip().split()
    dic[site] = pw

for _ in range(m):
    site = stdin.readline().strip()
    print(dic[site])
