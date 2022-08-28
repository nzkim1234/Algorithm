from sys import stdin

n = int(stdin.readline())

graph = [[0 for _ in range(n)] for _ in range(n)]
answer = 0


def is_possible(x, y):
    for i in range(n):
        if graph[i][y]:
            return False
    c_x = x
    c_y = y
    for _ in range(n):
        c_x -= 1
        c_y -= 1
        if c_x < 0 or c_y < 0:
            break
        else:
            if graph[c_x][c_y]:
                return False

    c_x = x
    c_y = y
    
    for _ in range(n):
        c_x -= 1
        c_y += 1
        if c_x < 0 or c_y > n - 1:
            break
        else:
            if graph[c_x][c_y]:
                return False
    return True

def queen(x, y, queen_num):
    global answer 
    if queen_num == n:
        answer += 1
    else:    
        for c_x in range(x, n):
            for c_y in range(n):
                if is_possible(c_x, c_y):
                    graph[c_x][c_y] = 1
                    queen(c_x + 1, c_y, queen_num + 1)
                    graph[c_x][c_y] = 0

queen(0, 0, 0)
print(answer)