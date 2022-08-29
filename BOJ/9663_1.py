from sys import stdin

n = int(stdin.readline())

graph = [0] * n
result = 0


def is_possible(num):
    for i in range(num):
        if graph[num] == graph[i] or abs(num - i) - abs(graph[num] - graph[i]) == 0:
            return False

    return True



def queen(num):
    global result
    if num == n:
        result += 1
        return
    
    for i in range(n):
        graph[num] = i
         
        if is_possible(num):
            queen(num + 1)



queen(0)

print(result)