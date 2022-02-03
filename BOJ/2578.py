from lib2to3.pgen2.token import GREATER
from sys import stdin

graph = []

for _ in range(5):
    one_line = list(map(int, stdin.readline().split()))
    graph.append(one_line)
bingo_nums = []

result = 0
count = 0
for _ in range(5):
    for num in list(map(int, stdin.readline().split())):
        if count >= 3:
            continue
        result += 1
        count = 0
        
        for row in range(5):
            row_sum = 0
            for col in range(5):
                if graph[row][col] == num:
                    graph[row][col] = 0
                row_sum += graph[row][col]
            if row_sum == 0:
                count += 1
        
        for col in range(5):
            col_sum = 0
            for row in range(5):
                col_sum += graph[row][col]

            if col_sum == 0:
                count += 1
        
        decrease_diagonal_sum = 0
        
        for decrease_diagonal in range(5):
            decrease_diagonal_sum += graph[decrease_diagonal][decrease_diagonal]
        
        if decrease_diagonal_sum == 0:
            count += 1

        increase_diagonal_sum = 0

        for increase_diagonal in range(5):
            increase_diagonal_sum += graph[increase_diagonal][4 - increase_diagonal]

        if increase_diagonal_sum == 0:
            count += 1

print(result)
            