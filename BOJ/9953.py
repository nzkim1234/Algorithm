from sys import stdin
from collections import deque

word = deque(list(stdin.readline().strip()))
find_word = list(stdin.readline().strip())

stack = []

while word:
    stack.append(word.popleft())
    if stack[-1] == find_word[-1] and len(stack) >= len(find_word):
        is_same = True

        for i in range(len(find_word)):
            if stack[len(stack) - len(find_word) + i] != find_word[i]:
                is_same = False

        if is_same:

            for _ in range(len(find_word)):
                stack.pop()

stack = ''.join(stack)

if stack:
    print(stack)
else:
    print("FRULA")
