## pypy3으로 실행시 정답:

n = int(input())
crane = list(map(int,input().split()))
crane.sort(reverse=True)
m = int(input())
box = list(map(int,input().split()))
box.sort(reverse=True)
count = 0
if crane[0] < box[0]:
    print(-1)
else:
    while len(box) != 0:
        j = 0
        i = 0
        while True:
            if len(box) == 0 or i >= len(crane) or j >= len(box):
                break
            if crane[i] >= box[j]:
                del box[j]
            else:
                j += 1
                i -= 1
            i += 1
        count += 1
    print(count)

'''
pypy3으로 실행시 정답:
n = int(input())
crane = sorted(list(map(int, input().split())),reverse=True)
m = int(input())
box = sorted(list(map(int, input().split())),reverse=True)
if box[0] > crane[0]:
    print(-1)
else:
    count = 0
    while True:
        if not box:
            break
        for i in range(len(crane)):
            for j in range(len(box)):
                if crane[i] >= box[j]:
                    del box[j]
                    break
        count += 1
    print(count)

'''
