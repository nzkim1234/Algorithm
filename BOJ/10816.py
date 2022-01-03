import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
ln = list(map(int, input().split()))
ln = Counter(ln)
m = int(input())
lm = list(map(int, input().split()))
for i in lm:
    print(ln[i], end=' ')
