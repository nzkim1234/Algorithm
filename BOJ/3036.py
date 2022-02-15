from sys import stdin
from copy import deepcopy

n = int(stdin.readline())

radius = list(map(int, stdin.readline().split()))  # 반지름 저장
result = []

num = [True for _ in range(1001)]  # 소수를 얻기위한 숫자 리스트
prime_num = []  # 소수가 들어갈 공간

# 소수 판별
for i in range(2, 1001):
    if num[i]:
        for j in range(i + i, 1001, i):
            num[j] = False

        prime_num.append(i)

# 첫번째 원의 약수들을 구하기
base = []

while  True:
    for p_n in prime_num:
        if radius[0] % p_n == 0:
            radius[0] = radius[0] // p_n
            base.append(p_n)
            break

    if radius[0] == 1:
        break

base.sort()

# 나머지 원들의 약수 구하고 결과 계산하기
for circle in radius[1::]:
    c1 = []
    c2 = deepcopy(base)

    # 비교할 원의 약수 구하기
    while True:
        for p_n in prime_num:
            if circle % p_n == 0:
                circle = circle // p_n
                c1.append(p_n)
                break

        if circle == 1:
            break
    
    # 배열의 길이가 더 짧은 쪽을 찾기
    if len(c1) < len(c2):
        min_len = deepcopy(c1)
    else:
        min_len = deepcopy(c2)
    
    # 같은 약수가 있으면 제거
    for i in min_len:
        if i in c1 and i in c2:
            c1.remove(i)
            c2.remove(i)
    
    # 리스트가 비어있으면 1 추가
    if not c1:
        c1.append(1)
    if not c2:
        c2.append(1)

    # 남은 약수들을 다시 곱해주기
    mul1 = 1
    mul2 = 1

    for mul in c1:
        mul1 *= mul

    for mul in c2:
        mul2 *= mul

    # 결과 계산
    result = str(mul2) + '/' + str(mul1)

    print(result)
