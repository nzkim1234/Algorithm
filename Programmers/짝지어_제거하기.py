def solution(s):
    answer = 0
    stack = []

    for i in s:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    if not stack:
        answer = 1

    return answer

s = 'baabaa'

print(solution(s))
