from sys import stdin

n, h = map(int ,stdin.readline().split())

top = [0] * (h + 1)
bottom = [0] * (h + 1)

# 해당하는 칸을 표시
for i in range(n):
    if i % 2:
        top[int(stdin.readline())] += 1
    else:
        bottom[h - int(stdin.readline()) + 1] += 1

# 누적 합 구하기
for i in range(h - 1, 0, -1):
    top[i] += top[i + 1]

for i in range(1, h + 1):
    bottom[i] += bottom[i - 1]

total = [0] * (h + 1)

for i in range(1, h + 1):
    total[i] = top[i] + bottom[i]

total = total[1:]
result = min(total)

print(result, total.count(result))
