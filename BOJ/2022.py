from sys import stdin
from math import sqrt

x, y, c = map(float,stdin.readline().split())
max_length = 3000000001
x_pow = pow(x, 2)
y_pow = pow(y, 2)
start = 1
end = max_length

while end - start > 0.000001:
    mid = (start + end) / 2

    if x_pow - pow(mid, 2) <= 0 or y_pow - pow(mid, 2) <= 0:
        end = mid - 0.000001
        continue

    x_height = sqrt(x_pow - pow(mid, 2))
    y_height = sqrt(y_pow - pow(mid, 2))
    new_c = (x_height * y_height) / (x_height + y_height)
    
    if new_c >= c:
        start = mid + 0.000001
    else:
        end = mid - 0.000001
        
print(mid)