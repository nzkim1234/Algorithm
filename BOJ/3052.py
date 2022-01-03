g = []
for _ in range(10):
    g.append(int(input()) % 42)
g = set(g)
print(len(g))
