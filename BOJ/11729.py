from sys import stdin

k = int(stdin.readline())


def hanoi(num, a, b, c):
    if num == 1:
        print(str(a) + ' ' + str(c))
    else:
        hanoi(num -1, a, c, b)
        
        print(str(a) + ' ' + str(c))

        hanoi(num -1, b, a, c)


print(pow(2, k) - 1)

hanoi(k, 1, 2, 3)