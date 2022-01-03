n = int(input())
t = int(input())
photo_wall_num = []
photo_wall_recommended = []
for i in list(map(int, input().split())):
    if len(photo_wall_num) < n and (not i in photo_wall_num): # photo_wall 이 비어있고 i가 photo_wall에 없을 시
        photo_wall_num.append(i) # photo_wall에 i 추가
        photo_wall_recommended.append(1) #i의 추천수 1 증가
    else:
        if i in photo_wall_num: # i 가 photo_wall에 있을 시 추천수 1증가
            photo_wall_recommended[photo_wall_num.index(i)] += 1
        else:
            index = photo_wall_recommended.index(min(photo_wall_recommended)) # 제일 추천수가 적은 사람의 index 가져오기
            photo_wall_num.pop(index) #가져온 index pop
            photo_wall_num.append(i) #새로운 i를 photo_wall에 추가
            photo_wall_recommended.pop(index) #가져온 index pop
            photo_wall_recommended.append(1) # 추천수 1 증가
print(*sorted(photo_wall_num))
