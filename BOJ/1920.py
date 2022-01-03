n = int(input())
arr_n = sorted(list(map(int, input().split())))
m = int(input())
arr_m = list(map(int, input().split()))


def find(i, s, e):
    m = (s+e)//2
    if s > e:
        print(0)
        return
    elif arr_n[m] > i:
        e = m - 1
    elif arr_n[m] < i:
        s = m + 1
    elif arr_n[m] == i:
        print(1)
        return
    find(i, s, e)


for i in arr_m:
    find(i, 0, n-1)
