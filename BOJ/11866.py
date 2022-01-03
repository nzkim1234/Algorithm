n, k = map(int, input().split())
line = [i+1 for i in range(n)]
count = 1
point = 0
answer = []
while n > 0:
    if count >= k:
        answer.append(line[point])
        del line[point]
        point -= 1
        count = 0
        n -= 1
    count += 1
    point += 1
    if point >= n:
        point = 0
print("<", end='')
for i in range(len(answer)-1):
    print(str(answer[i]) + ", ", end='')
print(str(answer[-1]) + ">")
