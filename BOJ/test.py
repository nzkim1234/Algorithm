rooms = { 'R1' : ['R2', 0, 0, 0], 'R2' : ['R3', 0, 'R1', 0], 'R3' : ['R6', 'R4', 'R2', 'R5'], 'R4': [0, 0, 0, 'R3'], 'R5' : [0, 'R3', 0, 0], 'R6"' : [0, 0, 'R3', 0]}
start = 'R1'
a = ''

while True:
    exits = []
    
    for i in range(len(rooms[start])):
        if rooms[start][i] != 0:
            if i == 0:
                exits.append('north')
            elif i == 1:
                exits.append('west')
            elif i == 2:
                exits.append('south')
            else:
                exits.append('east')
            
    print(f"You are in {start}, exits: ", end = '')
    print(*exits)

    a = input(">")

    if a == 'north':
        a = 0
    elif a =='west':
        a = 1
    elif a == 'south':
        a = 2
    elif a == 'east':
        a = 3
    
    start = rooms[start][a]