n = int(input())
me = int(input())
if n == 1:
    print(0)
    quit()
a = []
for i in range(n-1):
    a.append(int(input()))
count = 0
change = 0
while True:
    a.sort(reverse=True)
    if me <= a[0]:
        me += 1
        a[0] -= 1
        count += 1
    else:
        break
print(count)
