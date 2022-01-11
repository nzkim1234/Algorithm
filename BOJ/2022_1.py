from sys import stdin
from math import sqrt

x, y, c = map(float,stdin.readline().split())
x_pow = pow(x, 2)
y_pow = pow(y, 2)
start = 1
end = 3000000001

while end - start > 0.000001:
    mid = (start + end) / 2

    # 높이의 값이 범위 밖일 때
    if x_pow - pow(mid, 2) <= 0 or y_pow - pow(mid, 2) <= 0:
        end = mid - 0.000001
        continue
    
    # x의 직선의 방정식 구하기
    x_height = sqrt(x_pow - pow(mid, 2))
    x_point1 = [0, x_height]
    x_point2 = [mid, 0]
    # y = ax + b
    x_a = -(x_height / mid)
    x_b = x_height

    # y의 직선의 방정식 구하기
    y_height = sqrt(y_pow - pow(mid, 2))
    y_point1 = [0, 0]
    y_point2 = [mid, y_height]    
    # y = ax + b
    y_a = (y_height / mid)
    y_b = 0

    #교점(intersection_point) 구하기
    intersection_point = x_height * (mid / (x_height + y_height))
    
    # 교점의 y좌표 구하기
    new_c = x_a * intersection_point + x_b

    if new_c >= c:
        start = mid + 0.000001
    else:
        end = mid - 0.000001
  
print(mid)