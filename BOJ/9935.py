from sys import stdin
from collections import deque

word = deque(list(stdin.readline().strip()))
find_word = list(stdin.readline().strip())

stack = []

while word:
    stack.append(word.popleft())

    # stack[-1]이 찾는 단어의 마지막 글자와 같고 len(stack) >= len(find_word)일 때
    if stack[-1] == find_word[-1] and len(stack) >= len(find_word):
        is_same = True

        # 각 글자를 비교하다가 서로 문자가 다르면 break
        for i in range(len(find_word)):
            if stack[len(stack) - len(find_word) + i] != find_word[i]:
                is_same = False
                break
            
        # is_same이 참이면 글자 길이만큼 pop하기
        if is_same:
            for _ in range(len(find_word)):
                stack.pop()

stack = ''.join(stack)

if stack:
    print(stack)
else:
    print("FRULA")
