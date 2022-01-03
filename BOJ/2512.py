n = int(input())
money = list(map(int, input().split()))
m = int(input())
if sum(money) <= m: # 모든 금액의 총합이 예산보다 적을 경우 최대 금액을 출력
    print(max(money))
else:
    # 이분 탐색
    s = 1
    e = m
    while s <= e:
        total_price = 0
        mid = (s+e) // 2
        for i in money: 
            if i > mid: # i 가 mid(최대 예산) 값 보다 클시 mid(최대 예산) 을 total price에 더하기
                total_price += mid
            else: # 아닐시 i의 값을 total price에 더하기
                total_price += i
        if total_price > m: # total price 가 m보다 클시 e 값을 줄이기
            e = mid - 1
        else: # total price 가 m보다 작을 시 s 값 늘이기
            s = mid + 1
    print(e)