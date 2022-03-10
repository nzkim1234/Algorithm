from sys import stdin

graph = [True] * 10001

for i in range(1, 10001):
    num_len = len(str(i))
    new_num = i

    for j in range(num_len - 1, -1, -1):
        new_num += i // pow(10, j)
        i = i % pow(10, j)
    
    if new_num < 10001:
        graph[new_num] = False

for i in range(10001):
    if graph[i]:
        print(i)