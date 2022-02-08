from sys import stdin

n = int(stdin.readline())

graph = list(map(int, stdin.readline().split()))
stack = []
result = []

for i in range(n):
    num = graph[i]
    
    # 스택이 비어있으면
    if not stack:
        result.append(0)
        stack.append([i + 1, num])

    else:
        # 스택의 값이 자기보다 클 때까지 스택 pop
        while stack and num > stack[-1][1]:
            stack.pop()

        # 스택이 비어있으면
        if not stack:
            result.append(0)
        else:            
            result.append(stack[-1][0])
    
        stack.append([i + 1, num])  # 스택 추가

print(*result)