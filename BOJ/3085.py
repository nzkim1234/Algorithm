from sys import stdin

n = int(stdin.readline())

graph = []

for _ in range(n):
    graph.append(list(map(str,stdin.readline().strip())))

position = [[0, 1], [1, 0]]
result = 0

for i in range(n):
    for j in range(n):
        for p_x, p_y in position:
            n_x = i + p_x
            n_y = j + p_y
            current_result = 0

            if 0<= n_x < n and 0 <= n_y < n:
                #if graph[i][j] != graph[n_x][n_y]:
                change_value = graph[i][j]
                graph[i][j] = graph[n_x][n_y]
                graph[n_x][n_y] = change_value

                for x in range(n):
                    result = max(
                        result,
                        graph[x].count('P'),
                        graph[x].count('C'),
                        graph[x].count('Z'),
                        graph[x].count('Y'),
                    )
                    
                for y in range(n):
                    candy_dic = {'P': 0, 'C':0, 'Z':0, 'Y':0}

                    for f_x in range(n):
                        candy_dic[graph[f_x][y]] += 1
                        
                    result = max(result, max(candy_dic.values()))
                
                change_value = graph[i][j]
                graph[i][j] = graph[n_x][n_y]
                graph[n_x][n_y] = change_value

print(result)


