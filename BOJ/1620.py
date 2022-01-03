import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = []
n_dic = {}
for i in range(n):
    pk = input().rstrip()
    n_list.append(pk)
    n_dic[pk] = i + 1
for _ in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(n_list[int(q)-1])
    else:
        print(n_dic[q])
