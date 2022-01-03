arr = []
for _ in range(9):
    arr.append(int(input()))
print(max(arr), arr.index(max(arr))+1)
