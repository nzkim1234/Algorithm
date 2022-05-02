from sys import stdin

n = int(stdin.readline())
graph = [[0 for _ in range(8)] for _ in range(8)]

def n_queen(x, y, num):
    p_x = x
    p_y = y