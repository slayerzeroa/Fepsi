y, x = map(int, input().split())

chess_map = []
for _ in range(y):
    field = list(input())
    chess_map.append(field)

# 시작점 구해주기
start_point = []
for a in range(y-7):
    for b in range(x-7):
        start_point.append([a, b])

# 체크리스트 생성
check_list = [0 for x in range(len(start_point))]

# 시작점 개수만큼 반복
index = 0
for y, x in start_point:
    for i in range(8-1):
        if chess_map[y][x + i] == chess_map[y][x + i + 1]:
            if chess_map[y][x + i] == 'W':
                chess_map[y + 1][x + i] = 'B'
            else:
                chess_map[y + 1][x + i] = 'W'
            check_list[index] += 1
        for j in range(8-1):
            if chess_map[y+j][x+i] == chess_map[y+j+1][x+i]:
                if chess_map[y+j][x+i] == 'W':
                    chess_map[y+j+1][x+i] = 'B'
                else:
                    chess_map[y+j+1][x+i] = 'W'
                check_list[index]+=1
    index += 1

print(min(check_list))