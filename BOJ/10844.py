from sys import stdin

n = int(stdin.readline())

print((n + pow(2,n-1) * 7 + 1) % 1000000000)