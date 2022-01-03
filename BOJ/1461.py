n, m = map(int, input().split())
n_l = list(map(int, input().split()))
plusn = []
minusn = []
for i in n_l:
    if i > 0:
        plusn.append(i)
    else:
        minusn.append(abs(i))
plusn.sort(reverse= True)
minusn.sort(reverse= True)
footstep = []
c = 0
for i in minusn:
    if c % m == 0:
        footstep.append(i)
    c += 1
c = 0
for i in plusn:
    if c % m == 0:
        footstep.append(i)
    c += 1
footstep.sort(reverse= True)
result = footstep[0]
for i in footstep[1:]:
    result += i * 2
print(result)
