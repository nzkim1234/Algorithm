from sys import stdin
import heapq

n = int(stdin.readline())
presents = []

for _ in range(n):
    a = list(map(int, stdin.readline().split()))

    # a가 0일 경우
    if a[0] == 0:
        # 선물에 값이 있을 경우 heappop으로 선물의 값 출력
        if presents:
            print(-heapq.heappop(presents))  # 최소 힙 조건을 위해 저장할때 -(음수)로 바꿨으므로 다시 -를 붙여 양수로 변환
        # 없을 경우 -1 출력
        else:
            print(-1)

    # 0이 아닐 경우
    else:
        # a의 인덱스 1부터 끝까지 힙에 저장, (heap은 최소힙이므로 -(음수)로 바꾸어서 저장)
        for i in a[1::]:
            heapq.heappush(presents, -i)
