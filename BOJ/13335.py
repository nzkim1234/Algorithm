from collections import deque

n, w, l = map(int, input().split())
a = deque(map(int, input().split()))
bridge = deque([0] * w) # 다리의 길이만큼 덱 생성(트럭은 오른쪽-> 왼쪽으로 이동 하기 때문에 다리의 끝은 [0], 시작은 [-1])
t = 0 # 시간
while a:
    t += 1
    bridge.popleft() # 다리의 끝(건너는 마지막 자리)를 pop하기
    if sum(bridge) + a[0] <= l: # 올라가야할 a(트럭)의 무게 + 현재 다리의 무게가 다리의 최대하중 이하일시
        bridge.append(a.popleft()) # 다리의 시작에 a(a의 무게)를 올린다
    else: # 아닐 시 그냥 다리의 시작을 추가
        bridge.append(0)
while sum(bridge) > 0: # a(트럭)가 전부 다리에 올라갔어도 아직 다리에 a(트럭)가 남아있을 수 있기때문에 사용
    t += 1
    bridge.popleft()
print(t)