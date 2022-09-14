def solution(n, k):
    answer = 0
    change = ""

    while n != 0:
        change += str(n % k)
        n = n // k

    change = "".join(list(reversed(change))).split('0')
    
    for i in change:
        if i != '':
            i = int(i)
            is_prime = True
            if i == 1:
                is_prime = False
            else:
                for j in range(2, int(i ** 0.5)+ 1):
                    if i % j == 0:
                        is_prime = False
            if is_prime:
                answer += 1 
                
    return answer


print(solution(437674, 3))
print(solution(110011, 10))