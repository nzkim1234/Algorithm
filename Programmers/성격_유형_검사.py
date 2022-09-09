def solution(survey, choices):
    answer = []
    graph = {'RT': {'R':0, 'T':0}, 'CF': {'C':0, 'F':0}, 'JM': {'J':0, 'M':0}, 'AN': {'A':0, 'N':0}}
    
    for i, a in enumerate(survey):
        if a in graph:
            if choices[i] == 1:
                graph[a][a[0]] += 3
            elif choices[i] == 2:
                graph[a][a[0]] += 2
            elif choices[i] == 3:
                graph[a][a[0]] += 1
            elif choices[i] == 4:
                graph[a][a[0]] += 0
            elif choices[i] == 5:
                graph[a][a[1]] += 1
            elif choices[i] == 6:
                graph[a][a[1]] += 2
            elif choices[i] == 7:
                graph[a][a[1]] += 3
        else:
            a = "".join(reversed(a))

            if choices[i] == 1:
                graph[a][a[1]] += 3
            elif choices[i] == 2:
                graph[a][a[1]] += 2
            elif choices[i] == 3:
                graph[a][a[1]] += 1
            elif choices[i] == 4:
                graph[a][a[1]] += 0
            elif choices[i] == 5:
                graph[a][a[0]] += 1
            elif choices[i] == 6:
                graph[a][a[0]] += 2
            elif choices[i] == 7:
                graph[a][a[0]] += 3

    for a in graph.values():
        key1, key2 = a.keys()
        value1, value2 = a.values()

        if value1 < value2:
            answer.append(key2)
        else:
            answer.append(key1)

    answer = "".join(answer)

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
