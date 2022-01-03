a = int(input())
b = int(input())
c = int(input())
r = str(a*b*c)
g = [0] * 10
for i in range(len(r)):
    g[int(r[i])] += 1
for i in g:
    print(i)
