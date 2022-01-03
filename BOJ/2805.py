import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = max(arr)
while start <= end:
    total = 0
    mid = (start+end) // 2
    total = sum(i-mid if i > mid else 0 for i in arr)
    if total < m:
        end = mid - 1
    else:
        start = mid + 1
print(end)
