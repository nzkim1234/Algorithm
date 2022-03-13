from sys import stdin

n, r, c = map(int ,stdin.readline().split())
count = 0

def z(n, x, y):
    global count 
    if x == r and y == c:
        print(count)
        quit()
    
    if n == 1:
        count += 1
        return 
    
    if not (x <= r < x + n and y <= c < y + n):
        count += n * n
        return
    
    z(n // 2, x, y)
    z(n // 2, x, y + n // 2)
    z(n // 2, x + n // 2, y)
    z(n // 2, x + n // 2, y + n // 2)

z(pow(2, n), 0, 0)