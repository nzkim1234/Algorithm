n, l = map(int, input().split())
count = 1
location = list(map(int, input().split()))
location.sort()
pipe = location[0] + l - 1
for i in location:
    if i > pipe:
        pipe = i + l - 1
        count += 1
print(count)
