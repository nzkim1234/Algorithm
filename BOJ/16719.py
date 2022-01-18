from sys import stdin
 
word = list(stdin.readline().strip())
result = [''] * len(word)
 
def func(string, start):
    if not string:
        return

    index = string.index(min(string))  # 제일 작은 알파벳의 인덱스 찾기
    result[start + index] = min(string)  # 알파벳을 결과리스트에 저장

    print("".join(result))

    func(string[index + 1:], start + index + 1)  # 찾은 인덱스의 뒤쪽을 탐색
    func(string[:index], start)  # 찾은 인덱스의 앞쪽을 탐색
 
func(word, 0)