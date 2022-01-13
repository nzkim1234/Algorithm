from sys import stdin

n1, n2 = map(int, stdin.readline().split())

n1_list = list(reversed(list(stdin.readline().strip())))
n2_list = list(stdin.readline().strip())
big_list = n1_list + n2_list
big_list_direction = ['r'] * n1 + ['l'] * n2


t = int(stdin.readline())

for _ in range(t):
    index = 0

    while index <= len(big_list) - 2:
        if big_list_direction[index] == 'r' and big_list_direction[index + 1] == 'l':
            exchange = [big_list_direction[index], big_list[index]]

            big_list_direction[index] = big_list_direction[index + 1]
            big_list[index] = big_list[index + 1]

            big_list_direction[index + 1] = exchange[0]
            big_list[index + 1] = exchange[1]

            index += 2
        else:
            index += 1

print(''.join(big_list))