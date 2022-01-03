line = input().upper()
word = list(set(line))
arr = []
for i in word:
    arr.append(line.count(i))
result = max(arr)
if arr.count(result) > 1:
    print('?')
else:
    print(word[arr.index(result)])
