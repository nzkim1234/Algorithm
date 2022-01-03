def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    for i in A:
        for j in range(len(B) - 1, -1, -1):
            if B[j] > i:
                del B[j]
                answer += 1
                break
    return answer

A = [5,1,3,7]
B = [2,2,6,8]

print(solution(A,B))