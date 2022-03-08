from sys import stdin

n = int(stdin.readline())
dic = {}

for i in range(n):
    dic[i+1] = int(stdin.readline())

while True:
    baseSet = set(dic.values())
    dic = {key:value for key, value in dic.items() if key in baseSet}
    if baseSet == set(dic.values()):
        break

print(len(dic))

for key in dic.keys():
    print(key)
