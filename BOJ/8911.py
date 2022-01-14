from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    turtle = [0, 0]
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    index = 0
    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0
    command = list(map(str,stdin.readline().strip()))
    
    for i in command:
        if i == 'F':
            turtle[0] += direction[index][0]
            turtle[1] += direction[index][1]
            max_x = max(max_x, turtle[0])
            max_y = max(max_y, turtle[1])
            min_x = min(min_x, turtle[0])
            min_y = min(min_y, turtle[1])
        elif i == 'B':
            turtle[0] -= direction[index][0]
            turtle[1] -= direction[index][1]
            max_x = max(max_x, turtle[0])
            max_y = max(max_y, turtle[1])
            min_x = min(min_x, turtle[0])
            min_y = min(min_y, turtle[1])
        elif i == 'L':  
            index -= 1
            if index < 0:
                index = 3
        else:
            index += 1
            if index > 3:
                index = 0

    print((max_x - min_x) * (max_y - min_y))