from sys import stdin

n, kjm, lhs, = map(int, stdin.readline().split())
count = 0

while True:
    count += 1

    # 종료 조건은 큰수 - 작은수 == 1,
    # 같이 대결을 하기 위해서는 큰수가 2의 배수여야함
    if max(kjm, lhs) % 2 == 0 and abs(kjm - lhs) == 1:
        break
    
    # 계산의 편의를 위해 2의 배수로 변환
    if kjm % 2 != 0:
        kjm += 1
    
    kjm = kjm // 2 

    # 계산의 편의를 위해 2의 배수로 변환
    if lhs % 2 != 0:
        lhs += 1
    
    lhs = lhs // 2 

    # 부전승이 있을 경우
    if n % 2:
        n += 1

    n = n // 2

print(count)
