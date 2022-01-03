from sys import stdin

n = int(stdin.readline())
presents = []

for _ in range(n):
    a = list(map(int, stdin.readline().split()))

    # a가 0일 경우
    if a[0] == 0:
        # 선물에 값이 있을 경우 pop하기
        if presents:
            print(presents.pop())
        # 없을 경우 -1 출력
        else:
            print(-1)

    # 0이 아닐 경우
    else:
        # a의 인덱스 1부터 끝까지 저장
        for i in a[1::]:
            presents.append(i)

        presents.sort()  # 정렬하기
