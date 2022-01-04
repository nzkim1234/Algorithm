def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    
    # B[j] 값이 i보다 클경우 B[j]를 삭제
    for i in A:
        for j in range(len(B) - 1, -1, -1):
            if B[j] > i:
                answer += 1
                B.pop()
                break

    return answer

A = [5,1,3,7]
B = [2,2,6,8]

print(solution(A,B))
