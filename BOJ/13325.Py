from sys import stdin

k = int(stdin.readline())
line = [0] + list(map(int, stdin.readline().split()))
tree = [0 for _ in range(pow(2, k))]

for i in range(len(tree) - 1, 0, -1):
    if i <= pow(2, k - 1) - 1:
        tree[i] = max(line[i * 2] + tree[i * 2 + 1] , 
        line[i * 2 - 1] + tree[i * 2])

        for j in range(i * 2 - 1, i * 2 + 1):    
            
            if j % 2: r = 0
            else: r = 1

            if line[j] < tree[i] - tree[i * 2 + r]:
                line[j] = tree[i] - tree[i * 2 + r]
    else:
        tree[i] = max(line[i * 2] , line[i * 2 - 1])
        
        for j in range(i * 2 - 1, i * 2 + 1):
            if line[j] <= tree[i]:
                line[j] = tree[i]

print(sum(line))