def solution(survey, choices):
    graph = {'RT': {'R':0, 'T':0}, 'CF': {'C':0, 'F':0}, 'JM': {'J':0, 'M':0}, 'AN': {'A':0, 'N':0}}
    for i, a in enumerate(survey):
        print("".join(reversed(a)))
        if a in graph:
            if choices[i] < 4:
                graph[a][a[0]] += 1
            elif choices[i] > 4:
                graph[a][a[1]] += 1
        else:
            a = "".join(reversed(a))
            if choices[i] < 4:
                graph[a][a[1]] += 1
            elif choices[i] > 4:
                graph[a][a[0]] += 1
    answer = ''
    return answer