r, c, k = map(int, input().split())
table = []
for _ in range(3):
    table.append(list(map(int, input().split())))
time = 0
while True:
    if time > 100:
        print(-1)
        break
    l_r = len(table)
    l_c = len(table[0])
    if l_r > r-1 and l_c > c-1:
        if table[r-1][c-1] == k:
            print(time)
            break
    if l_r >= l_c:
        # r 연산
        max_l = 0
        new_list = [[] for _ in range(l_r)]
        for i in range(l_r):
            num_list = set(table[i])
            if 0 in num_list:
                num_list.remove(0)
            new_table = []
            for j in num_list:
                new_table.append([j, table[i].count(j)])
            new_table.sort()
            new_table.sort(key = lambda x : x[1])
            for a, b in new_table:
                new_list[i].append(a)
                new_list[i].append(b)
                if len(new_list) > 100:
                    break
            max_l = max(max_l, len(new_list[i]))
        for i in range(l_r):
            while len(new_list[i]) < max_l:
                new_list[i].append(0)
            table[i] = new_list[i]
    else:
        # c 연산
        max_l = 0
        new_list = [[] for _ in range(l_c)]
        get_table = [[] for _ in range(l_c)]
        for i in range(l_c):
            g_t = [j[i] for j in table]
            num_list = set(g_t)
            if 0 in num_list:
                num_list.remove(0)
            new_table = []
            for j in num_list:
                new_table.append([j, g_t.count(j)])
            new_table.sort()
            new_table.sort(key = lambda x : x[1])
            for a, b in new_table:
                new_list[i].append(a)
                new_list[i].append(b)
                if len(new_list) > 100:
                    break
            max_l = max(max_l, len(new_list[i]))
        for i in range(l_c):
            while len(new_list[i]) < max_l:
                new_list[i].append(0)
        result_table = [[0 for _ in range(len(new_list))] for _ in range(len(new_list[i]))]
        x = 0
        for i in new_list:
            y = 0
            for j in i:
                result_table[y][x] = j
                y += 1
            x += 1
        table = result_table
    time += 1
