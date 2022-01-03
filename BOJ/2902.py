s = list(map(int, input().split()))
a = [1, 2, 3, 4, 5, 6, 7, 8]
d = [8, 7, 6, 5, 4, 3, 2, 1]
if s == a:
    print('ascending')
elif s == d:
    print('descending')
else:
    print('mixed')
