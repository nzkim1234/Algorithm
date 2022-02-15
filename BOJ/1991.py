from sys import stdin

n = int(stdin.readline())
graph = [[chr(ord('A') + i), 0, 0] for i in range(26)]

for _ in range(n):
    parent, child1, child2 = stdin.readline().strip().split()

    if child1 != '.':
        graph[ord(parent) - 65][1] = child1
    if child2 != '.':
        graph[ord(parent) - 65][2] = child2

preorder_traversal = []
inorder_traversal = []
postorder_traversal = []

def order(node):
    p, c1, c2 = node

    preorder_traversal.append(p)

    if c1 != 0:
        order(graph[ord(c1) - 65])

    inorder_traversal.append(p)

    if c2 != 0:
        order(graph[ord(c2) - 65])
    
    postorder_traversal.append(p)
    

order(graph[0])

print("".join(preorder_traversal))
print("".join(inorder_traversal))
print("".join(postorder_traversal))
