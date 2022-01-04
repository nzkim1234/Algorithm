def solution(s):
    answer = 0
    stack = []

    # 하나씩 stack에 추가, 새로 추가되는 글자가 stack[-1]의 값과 같을 시 stack.pop() 아닐시  stack.append(글자)
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
