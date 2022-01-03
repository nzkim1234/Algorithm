from sys import stdin

string = stdin.readline()
queue = []
result = 0

try:
    for check in string:
        if check == '(' or check == '[':  # 열리는 괄호면 큐에 추가
            queue.append(check)

        elif check == ')':  # 닫히는 괄호일 때
            # 열리는 괄호가 나올때까지 큐에서 pop, 숫자가 나올시 r에 더하기
            r = 0
            a = queue.pop()

            while a != '(':
                r += int(a)
                a = queue.pop()

            if r == 0:
                r = 1
            
            #최종 결과를 큐에 저장
            queue.append(str(r * 2))
        
        elif check == ']':  # 닫히는 괄호일 때
            # 열리는 괄호가 나올때까지 큐에서 pop, 숫자가 나올시 r에 더하기
            r = 0
            a = queue.pop()

            while a != '[':
                r += int(a)
                a = queue.pop()

            if r == 0:
                r = 1

            #최종 결과를 큐에 저장
            queue.append(str(r * 3))

    # 큐에 남아있는 값을 result에 추가
    for check in queue:
        result += int(check)

    print(result)

except:
    print(0)
