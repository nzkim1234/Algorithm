#PyPy3

from sys import stdin

n = int(stdin.readline())

count = 0
graph = [0] * n


def is_promising(x):
    for i in range(x):

        # 같은 행이고 같은 대각선일 경우 false 리턴
        if graph[x] == graph[i] or abs(graph[x] - graph[i]) == abs(x - i):
            return False
    
    return True


def place_queens(x):
    global count

    # n개를 배치했으면 count += 1
    if x == n:
        count += 1
        return

    for i in range(n):
        graph[x] = i  # x열 i행에 퀸을 배치

        if is_promising(x):
            place_queens(x + 1)


place_queens(0)

print(count)
