from sys import stdin

n = int(stdin.readline())

serial_nums = []

for _ in range(n):
    serial_num = stdin.readline().strip()
    count_num = 0
    for num in serial_num:
        if '0' <= num <= '9':
            count_num += int(num)
    serial_nums.append([serial_num, len(serial_num), count_num])

serial_nums.sort(key = lambda x : (x[1], x[2], x[0]))

for i in serial_nums:
    print(i[0])
