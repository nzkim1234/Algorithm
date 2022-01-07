from sys import stdin

n, p = map(int, stdin.readline().split())
count = 0

lines = [[],[],[],[],[],[]]

for _ in range(n):
    line_n, fret = map(int, stdin.readline().split())
    if not lines[line_n-1]:
        lines[line_n-1].append(fret)
        count += 1
    else:
        if lines[line_n-1][-1] < fret:
            lines[line_n-1].append(fret)
            count +=1
        elif lines[line_n-1][-1] > fret:
            while lines[line_n-1][-1] > fret:
                lines[line_n-1].pop()
                count += 1
                if not lines[line_n - 1]:
                    break
            if not lines[line_n - 1]:
                lines[line_n-1].append(fret)
                count += 1
            elif not lines[line_n-1][-1] == fret:
                lines[line_n-1].append(fret)
                count += 1

print(count)