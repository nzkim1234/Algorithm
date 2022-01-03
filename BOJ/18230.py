n, na, nb = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
result = 0
if n % 2 != 0:
    result += a[-1]
    del a[-1]
    na -= 1
for i in range(n//2):
    if na >= 2:
        ma = a[-1] + a[-2] 
    else:
        ma = 0
    if nb >= 1:
        mb = b[-1]
    else:
        mb = 0
    if mb < ma:
        result += ma
        del a[-1]
        del a[-1]
        na -= 2
    else:
        result += mb
        del b[-1]
        nb -= 1
print(result)
