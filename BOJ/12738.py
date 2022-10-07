from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
result = [a[0]]

for i in a[1::]:
    if result[-1] < i:
        result.append(i)
    else:
        start = 0
        end = len(result) - 1

        while start <= end:
            mid = (start + end) // 2

            if result[mid] == i:
                start = mid
                break
            elif result[mid] > i:
                end = mid - 1
            else:
                start = mid + 1

        result[start] = i
        
print(len(result))