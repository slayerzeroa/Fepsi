angle_list = []     # 각도 리스트

for i in range(3):  # 3번 반복해서 각도 추가
    angle_list.append(int(input())) # 추가!!!!!!!!!!!!!!!!!!

if sum(angle_list) == 180:          # angle_list 원소들의 합이 180이면
    angle_set = set(angle_list)     # set으로 만들어주기
    if len(angle_set) == 1:         # set 원소가 1개면
        print("Equilateral")        # 정삼각형
    elif len(angle_set) == 2:       # set 원소가 2개면
        print("Isosceles")          # 이등변삼각형
    elif len(angle_set) == 3:       # set 원소가 3개면
        print("Scalene")            # 고냥 삼각형
else:                               # angle_list 원소들의 합이 180이 아니면
    print("Error")                  # Error 출력