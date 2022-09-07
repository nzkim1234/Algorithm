def solution(id_list, report, k):
    report = list(set(report))
    set_list, count, answer = [], {}, {}
    
    for name in id_list:
        count[name] = []
        answer[name] = 0
    
    for input in report:
        set_list.append(list(reversed((input.split()))))
    
    for a, b in set_list:
        count[a].append(b)
    
    for i in count:
        if len(count[i]) >= k:
            for j in count[i]:
                answer[j] += 1
                
    answer = list(answer.values())
    
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))