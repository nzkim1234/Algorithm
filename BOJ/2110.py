from sys import stdin

n, c = map(int, stdin.readline().split())
house = []

for _ in range(n):
    house.append(int(stdin.readline()))

house.sort()

start = 1  # 최소 거리
end = house[n - 1] - house[0]  # 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2
    current_range = house[0]
    count = 1

    for i in range(1, n):
        if house[i] >= current_range + mid:  # 거리가 더 길면 공유기 설치
            count += 1
            current_range = house[i]
    
    if count < c:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
        
print(result)
