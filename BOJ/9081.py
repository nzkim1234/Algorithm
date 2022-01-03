from sys import stdin

n = int(stdin.readline())
words = []

for i in range(n):
    word = list(stdin.readline().strip())
    
    # next_permuation 구현
    
    change_index_one = 0

    # 마지막 인덱스에서 첫번째까지 탐색하면서 word[j] > word[j - 1]인 값 찾기
    for j in range(len(word) - 1, -1, -1):
        if word[j] > word[j - 1]:
            change_index_one = j - 1
            break

    change_index_two = 0

    # 마지막 인덱스에서 첫번째까지 탐색하면서 word[j] > word[change_index_one]인 값 찾기
    for j in range(len(word) - 1, -1, -1):
        if word[j] > word[change_index_one]:
            change_index_two = j
            break
        
    if change_index_one < 0:  # word[j] > word[j - 1]인 값이 바뀌지 않았으면 next_permuation이 없다.
        result = "".join(word)
    else:
        word[change_index_one], word[change_index_two] = word[change_index_two], word[change_index_one]  # 두 인덱스의 값을 바꿔준다
        result = "".join(word[:change_index_one + 1]) + "".join(list(reversed(word[change_index_one + 1::])))  # change_index_one 뒤에오는 값들은 반전시켜서 합친다

    print(result)
    