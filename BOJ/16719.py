from sys import stdin
from collections import deque

string = list(map(str, stdin.readline().strip()))
sort_by_alpha = deque(sorted(string))
print(sort_by_alpha)

