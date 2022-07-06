from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    dic = dict()
    count = 1 

    for _ in range(n):
        clothes, item = stdin.readline().strip().split()

        # 옷 종류가 없을 시 Key 추가, 있을 시 clothes 추가
        if item in dic:
            dic[item].append(clothes)
        else:
            dic[item] = ['none', clothes]
    
    # 경우의 수 계산
    for key in dic.keys():
        count *= len(dic[key])

    print(count - 1)
