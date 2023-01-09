check_list = []         # 체크리스트 생성

for i in range(5):      # 5번 반복
    check_list.append(input().split())  # 체크리스트에 넣어주기

time_list = []      # 시간 리스트 생성

#print(check_list)


for i in range(4):      # 4번 반복 hh:mm
    if check_list[1][i][1] == '.' and check_list[2][i][1] == '.' and check_list[3][i][1] == '.':            # 각 나올 수 있는 경우의 수를 고려하여 분류해줌
        time_list.append('0')
    elif check_list[1][i][0] == '.' and check_list[1][i][1] == '.' and check_list[3][i][1] == '.' and check_list[3][i][2] == '.':
        time_list.append('2')
    elif check_list[1][i][0] == '.' and check_list[1][i][1] == '.' and check_list[3][i][0] == '.' and check_list[3][i][1] == '.':
        time_list.append('3')
    elif check_list[0][i][1] == '.' and check_list[2][i][1] == '#' and check_list[4][i][1] == '.' and check_list[3][i][1] == '.':
        time_list.append('4')
    elif check_list[1][i][1] == '.' and check_list[1][i][2] == '.' and check_list[3][i][0] == '.' and check_list[3][i][1] == '.':
        time_list.append('5')
    elif check_list[1][i][1] == '.' and check_list[1][i][2] == '.' and check_list[3][i][1] == '.':
        time_list.append('6')
    elif check_list[1][i][1] == '.' and check_list[3][i][1] == '.':
        time_list.append('8')
    elif check_list[1][i][1] == '.' and check_list[3][i][0] == '.' and check_list[3][i][1] == '.':
        time_list.append('9')

#print(time_list)


print(time_list[0]+time_list[1]+':'+time_list[2]+time_list[3])      # 분류된 결과를 출력