N = int(input())
worm_num_list = []
for _ in range(N):
    horizon, vertical, number = map(int, input().split())
    map_list = []
    for i in range(number):
        map_list.append(list(map(int, input().split())))
    worm_num = len(map_list)
    map_list.sort(key=lambda x: (x[0], x[1]))
    for i in map_list:
        if [i[0]+1, i[1]] in map_list or [i[0], i[1]+1] in map_list:
            worm_num -= 1
        if [i[0]+1, i[1]] in map_list and [i[0], i[1]+1] in map_list and [i[0]+1, i[1]+1] in map_list:
            worm_num += 1
            #print(worm_num)
    worm_num_list.append(worm_num)

for i in worm_num_list:
    print(i)