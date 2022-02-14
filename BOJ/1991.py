from sys import stdin
from collections import deque

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

def preorder(node):
    p, c1, c2 = node

    preorder_traversal.append(p)

    if c1 != 0:
        preorder(graph[ord(c1) - 65])

    if c2 != 0:
        preorder(graph[ord(c2) - 65])


def inorder(node):
    p, c1, c2 = node
    
    if c1 != 0:
        inorder(graph[ord(c1) - 65])
    
    inorder_traversal.append(p)

    if c2 != 0:
        inorder(graph[ord(c2) - 65])


def postorder(node):
    p, c1, c2 = node
    
    if c1 != 0:
        postorder(graph[ord(c1) - 65])

    if c2 != 0:
        postorder(graph[ord(c2) - 65])
    
    postorder_traversal.append(p)
    

preorder(graph[0])
inorder(graph[0])
postorder(graph[0])

print("".join(preorder_traversal))
print("".join(inorder_traversal))
print("".join(postorder_traversal))