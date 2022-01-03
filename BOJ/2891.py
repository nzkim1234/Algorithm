n, s, r = map(int, input().split())
damaged = list(map(int, input().split()))
dummy = list(map(int, input().split()))
for i in range(r):
    for j in range(s):
        if(dummy[i] == damaged[j] or dummy[i] - damaged[j] == 1
           or dummy[i] - damaged[j] == -1):
            del damaged[j]
            s -= 1
            break
print(s)
