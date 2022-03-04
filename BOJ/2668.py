from sys import stdin

n = int(stdin.readline())
graph = [0]

for i in range(1, n + 1):
    graph.append(int(stdin.readline()))

value = 0
result = []

for i in range(1, n + 1):
    visit_graph = [False] * (n + 1)
    dict = {}

    for add_dict in range(n + 1):
        dict[add_dict] = 0
    
    if not visit_graph[i]:
        visit_graph[i] = True
        value = graph[i]
        dict[i] += 1
        dict[value] += 1

        while True:
            if not visit_graph[value]:
                visit_graph[value] = True
                dict[value] += 1
                value = graph[value]
                dict[value] += 1
            else:
                break

    can_be_result = []
    can_be = True
    for i in dict.items():
        if i[1] % 2 == 0:
            if i[1] != 0:
                can_be_result.append(i[0])
        else:
            can_be = False
            break
    
    if can_be:
        result += can_be_result

result = list(set(result))
print(len(result))
for i in result:
    print(i)