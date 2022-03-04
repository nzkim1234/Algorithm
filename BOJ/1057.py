from sys import stdin

n, kjm, lhs, = map(int, stdin.readline().split())
count = 0

while True:
    count += 1

    if max(kjm, lhs) % 2 == 0 and abs(kjm - lhs) == 1:
        break
    
    if kjm % 2 != 0:
        kjm += 1
    
    kjm = kjm // 2 

    if lhs % 2 != 0:
        lhs += 1
    
    lhs = lhs // 2 

    if n % 2:
        n += 1

    n = n // 2

print(count)