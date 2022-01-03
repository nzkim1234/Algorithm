from sys import stdin

king, stone, n = stdin.readline().split()
king_x, king_y = king
stone_x, stone_y = stone
chess_board = [[0 for _ in range(8)] for _ in range(8)]
king_loc = [int(king_y) - 1, ord(king_x) - 65]  # 문자를 숫자로 변환
stone_loc = [int(stone_y) - 1, ord(stone_x) - 65]  # 문자를 숫자로 변환
move_loc = []
movement = []

for _ in range(int(n)):
    movement.append(stdin.readline().strip())

for move in movement:
    new_king_loc = []
    new_stone_loc = []

    # 이동방향에 따라 이동
    if move == 'R':
        move_loc = [0, 1]
    elif move == 'L':
        move_loc = [0, -1]
    elif move == 'B':
        move_loc = [-1 , 0]
    elif move == 'T':
        move_loc = [1, 0]
    elif move == 'RT':
        move_loc = [1, 1]
    elif move == 'LT':
        move_loc = [1, -1]
    elif move == 'RB':
        move_loc = [-1, 1]
    elif move == 'LB':
        move_loc = [-1, -1]
        
    new_king_loc = [king_loc[0] + move_loc[0], king_loc[1] + move_loc[1]]  # 이동한 새로운 킹의 좌표

    if 0 <= new_king_loc[0] < 8 and 0 <= new_king_loc[1] < 8:  # 새로운 킹이 체스판 내부일 때
        if new_king_loc[0] == stone_loc[0] and new_king_loc[1] == stone_loc[1]:  # 새로운 킹의 좌표가 돌과 같을 때
            new_stone_loc = [stone_loc[0] + move_loc[0], stone_loc[1] + move_loc[1]]  # 돌을 이동
            
            if 0 <= new_stone_loc[0] < 8 and 0 <= new_stone_loc[1] < 8: # 이동한 새로운 좌표가 체스판 내부이면 킹, 돌의 좌표 저장
                king_loc = new_king_loc
                stone_loc = new_stone_loc
        else:  # 새로운 킹의 좌표가 돌과 같지 않을 때
            king_loc = new_king_loc  # 좌표 저장
    
king = chr(king_loc[1] + 65) + str(king_loc[0] + 1)  # 숫자를 문자로 변환
stone = chr(stone_loc[1] + 65) + str(stone_loc[0] + 1)  # 숫자를 문자로 변환

print(king)
print(stone)
