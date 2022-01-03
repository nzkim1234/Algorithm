s = input()
arr = [-1] * 26
for i in range(len(s)):
    if arr[ord(s[i])-97] == -1:
        arr[ord(s[i])-97] = i
for i in arr:
    print(i, end=' ')
