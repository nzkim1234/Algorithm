from sys import stdin

n,c = map(int, stdin.readline().split())
num = []
count = []
num_and_count = []
_input = list(map(int, stdin.readline().split()))

# 입력받은 수를 하나씩 읽으면서 num에 추가, num에 이미 추가되어있을시 같은 인덱스의 count값 증가
for i in _input:
    if i in num:
        count[num.index(i)] += 1
    else:
        num.append(i)
        count.append(1)

# num과 count를 합치기
for i in range(len(num)):
    num_and_count.append([num[i], count[i]])

num_and_count.sort(reverse = True, key = lambda x : x[1])  # 자주나온 순서로 정렬하기

for result_num, result_count in num_and_count:
    print((str(result_num) +' ') * result_count, end = '')
