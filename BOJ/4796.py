case = []
maximum = 0
while True:
    t = input()
    if t == "0 0 0":
        break
    l, p, v = map(int, t.split())
    maximum = 0
    maximum += v // p * l
    v = v - (v // p) * p
    if v > l:
        maximum += l
    else:
        maximum += v
    case.append(maximum)
count = 1
for i in case:
    print("Case " + str(count) + ": " + str(i))
    count += 1
