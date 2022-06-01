from sys import stdin

k = int(stdin.readline())

line = list(map(int, stdin.readline().split()))
tree = [0 for _ in range(pow(2, k ) - 1)]
print(line)
print(tree)
for i in range(len(tree) - 1, -1, -1):
    if i < pow(2, k - 1) - 1:
        if i == 0:
            print(line)
            print(tree)
            tree[i] = max(line[0] , line[1]) + tree[1]
            for j in range(2):
                if line[j] < tree[i] - tree[1]:
                    line[j] = tree[i] - tree[1]
        else:    
            tree[i] = max(line[i * 2] , line[i * 2 + 1]) + tree[i * 2 + 1]
            for j in range(i * 2, i * 2 + 2):    
                if line[j] < tree[i] - tree[i * 2 + 1]:
                    line[j] = tree[i] - tree[i * 2 + 1]
        print(tree[i])
        print(i)
        print('asdf')
    else:
        tree[i] = max(line[i * 2] , line[i * 2 + 1])
        for j in range(i * 2, i * 2 + 2):
            if line[j] < tree[i]:
                line[j] = tree[i]
print((line))
print(tree)