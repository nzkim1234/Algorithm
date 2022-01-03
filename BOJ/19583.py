import sys

s, e, q = sys.stdin.readline().split()
data = sys.stdin.readlines()

enter = []  # 입장 확인
exit = []  # 퇴장 확인


for a in data:
    time, name = a.split()  # a의 값을 time, name 으로 분리
    if time <= s:  # s시간보다 작거나 같을때 채팅을 쳤을 때 enter에 추가
        enter.append(name)
    elif e <= time <= q:  # e시간과 q시간 사이에 채팅을 쳤을 때 end에 추가
        exit.append(name)

enter = set(enter)  # 중복제거
exit = set(exit)  # 중복제거
result = 0

for i in enter:  # enter, end에 동시에 이름이 존재하면 result 증가
    if i in exit:
        result += 1

print(result)    
