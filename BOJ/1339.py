from sys import stdin
from string import ascii_uppercase

n = int(stdin.readline())
result = 0
alpha = {}

# alpha에 'A':0 꼴로 모든 알파벳 저장
for i in list(ascii_uppercase):
    alpha[i] = 0

words = []

# 알파벳의 자릿수의 값 만큼 알파벳에 해당하는 딕셔너리값 증가
for i in range(n):
    word = list(stdin.readline().strip())

    for i in range(len(word)):
        alpha[word[i]] += 10 ** (len(word) - i - 1)

list_alpha = []

# 딕셔너리의 값을 리스트로 변경
for i in alpha:
    list_alpha.append([i, alpha[i]])

# 변경된 값을 정렬
list_alpha.sort(key = lambda x : x[1], reverse = True)

# 계산하기
for i in range(10):
    result += list_alpha[i][1] * (9 - i)

print(result)
