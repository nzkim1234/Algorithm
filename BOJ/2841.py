from sys import stdin

n, p = map(int, stdin.readline().split())
count = 0

lines = [[],[],[],[],[],[]]

for _ in range(n):
    line_n, fret = map(int, stdin.readline().split())

    # 줄에 손가락이 없다면 줄에 손가락을 올린다.
    if not lines[line_n-1]:
        lines[line_n-1].append(fret)
        count += 1
        
    # 줄에 손가락이 있을 경우
    else:
        # 새로 잡는 프렛이 이전 프랫보다 높은 프렛이라면
        if lines[line_n-1][-1] < fret:
            lines[line_n-1].append(fret)
            count +=1
        
        # 새로 잡는 프렛이 이전 프랫보다 낮은 프렛이라면
        elif lines[line_n-1][-1] > fret:

            # 잡는 프렛이 새로 잡는 프랫과 같거나 작을 때까지 손가락을 땐다.
            while lines[line_n-1][-1] > fret:
                lines[line_n-1].pop()
                count += 1

                #프랫에 손가락이 없을 경우
                if not lines[line_n - 1]:
                    break
            
            # 줄에 손가락이 없을 경우
            if not lines[line_n - 1]:
                lines[line_n-1].append(fret)
                count += 1

            # 새로 잡는 프렛이 이전 프랫과 같지 않을 경우
            elif not lines[line_n-1][-1] == fret:
                lines[line_n-1].append(fret)
                count += 1

print(count)