import math

n = math.factorial(int(input()))
s = list(str(n))
s.reverse()
count = 0
for i in s:
    if i == str(0):
        count += 1
    else:
        break
print(count)
