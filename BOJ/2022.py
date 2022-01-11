from sys import stdin
from math import sqrt

x, y, c = map(float,stdin.readline().split())
x_pow = pow(x, 2)
y_pow = pow(y, 2)
start = 1
end = 3000000001

while end - start > 0.000001:
    mid = (start + end) / 2  # 밑변의 길이

    # 높이의 값이 범위 밖일 때
    if x_pow - pow(mid, 2) <= 0 or y_pow - pow(mid, 2) <= 0:
        end = mid - 0.000001
        continue
    
    # 높이 구하기
    x_height = sqrt(x_pow - pow(mid, 2))
    y_height = sqrt(y_pow - pow(mid, 2))
    
    # 교점의 높이 구하기
    new_c = (x_height * y_height) / (x_height + y_height)
    
    if new_c >= c:
        start = mid + 0.000001
    else:
        end = mid - 0.000001
        
print(mid)
