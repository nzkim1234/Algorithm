n = int(input())
start = [input().split() for _ in range(n)]
end = [input().split() for _ in range(n)]

result = 0

for i in range(n):
    for j in range(i,n):
        if start.index(end[i]) > start.index(end[j]):  # 시작할때의 인덱스가 끝날 때 자신의 뒤에 있는 차들보다 클때 result 추가
            result += 1
            break

print(result)
