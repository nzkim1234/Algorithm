from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

k = int(stdin.readline())
visited_node = list(map(int, stdin.readline().split()))
i = 0
tree = [False for i in range(pow(2, k) - 1)]  # 트리 생성


# 전위 순회 하면서 트리에 값 추가
def add_tree(num):
    global i
    if num * 2 <= len(tree):
        add_tree(num * 2)
    
    tree[num - 1] = visited_node[i]
    i += 1
    
    if num * 2 + 1 <= len(tree):
        add_tree(num * 2 + 1)
    

add_tree(1)

for i in range(k):
    print(*tree[pow(2, i) - 1 : pow(2, i + 1) - 1])
