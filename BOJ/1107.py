from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
broken_button = []

if m != 0:
    broken_button = list(map(int, stdin.readline().split()))

result = abs(100 - n)

for i in range(500000 * 2):
    num = list(map(int, str(i)))
    is_broken = False

    # 숫자에 고장난 버튼의 숫작 있을 경우 is_broken == false   
    for j in num:
        if j in broken_button:
            is_broken = True
            break
    
    if not is_broken:
        result = min(result, abs(n - i) + len(num))

print(result)