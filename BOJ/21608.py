from sys import stdin

n = int(stdin.readline())
graph = [[0 for _ in range(n)] for _ in range(n)]
student = []
position = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for _ in range(n*n):                    
    student.append(list(map(int, stdin.readline().split())))

for s, l1, l2, l3, l4 in student:
    like_student = [l1, l2, l3, l4]  # 학생이 좋아하는 학생을 like_student에 저장
    student_space = [0, 0, -1, -1]  # [x좌표, y좌표, 인접한 칸에 좋아하는 학생의 수, 인접한 칸에 빈칸]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:  # 칸이 비어있다면
                count_like_student = 0
                count_black_space = 0

                for p_x, p_y in position:  # 인접한 칸 탐색
                    n_x = i + p_x
                    n_y = j + p_y
                    
                    if 0 <= n_x < n and 0 <= n_y <n:
                        if graph[n_x][n_y] in like_student:  # 인접한 칸에 좋아하는 학생수를 구한다.
                            count_like_student += 1
                        elif graph[n_x][n_y] == 0:  # 인접한 칸에 빈칸의 수를 구한다.
                            count_black_space += 1

                # 인접한 칸에 좋아하는 학생이 더 많다 or 인접하는 칸에 좋아하는 학생의 수는 같지만 빈칸이 더 많을 때
                if student_space[2] < count_like_student or (student_space[2] <= count_like_student and count_black_space > student_space[3]):
                    student_space = [i, j, count_like_student, count_black_space]  # [x좌표, y좌표, 인접한 칸에 좋아하는 학생의 수, 인접한 칸에 빈칸] 저장

                
    graph[student_space[0]][student_space[1]] = s  # 최종적인 좌표에 학생을 배치

result = 0

# 결과 계산하기
for x in range(n):
    for y in range(n):
        student_list = []

        for l in student:
            if l[0] == graph[x][y]:
                student_list = l[1::]
                break

        count = 0

        for p_x, p_y in position:
            n_x = x + p_x
            n_y = y + p_y

            if 0 <= n_x < n and 0 <= n_y < n:
                if graph[n_x][n_y] in student_list:
                    count += 1
                    
        if count != 0:
            result += 10 ** (count - 1)
            
print(result)
