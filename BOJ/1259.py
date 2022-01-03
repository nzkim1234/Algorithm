while True:
    n = input()
    if n == '0':
        break
    if len(n) == 1:
        print('yes')
    for i in range(len(n)//2):
        if n[i] != n[len(n)-1-i]:
            print('no')
            break
        if i == len(n)//2-1:
            print('yes')
