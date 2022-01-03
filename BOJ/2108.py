import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
top_num = Counter(arr).most_common()
print("%.f" % (sum(arr)/n))
print(arr[n//2])
if n > 1:
    if top_num[0][1] == top_num[1][1]:
        print(top_num[1][0])
    else:
        print(top_num[0][0])
else:
    print(arr[0])
print(arr[-1] - arr[0])
