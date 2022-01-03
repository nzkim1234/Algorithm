n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
arr = sorted(set(arr))
arr = sorted(arr, key=(lambda x: len(x)))
for i in arr:
    print(i)
