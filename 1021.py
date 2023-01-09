# 회전큐 문제 회전큐 거리 계산 M - (n_1 - n_2), n_2 - n_1 # 이때 M의 큐의 크기, n_1,2는 노드의 숫자 # 삭제 시 N, n_1,2 업데이트 해주기

status = input().split()
m = int(status[0])
iterate = int(status[1])

num_list = input().split()
move = 0
num_list = list(map(int,num_list))

if abs(num_list[0] - 1) > m / 2:
    move += m - (num_list[0] - 1)
else:
    move += num_list[0] - 1
for j in range(len(num_list)):  # 리스트 조사
    if num_list[j] > num_list[0]:  # 만약 j번째 리스트 수가 i보다 크다면
        num_list[j] -= 1  # 1 감소

for i in range(iterate-1): # 반복횟수 설정
    if abs(num_list[i] - num_list[i+1])> m/2:
        if num_list[i] > num_list[i+1]: # 만약 앞에 수가 뒤에 수보다 크면
            move += m-(num_list[i]-num_list[i+1])-1 # M - (n_1 - n_2) - 1
        else:   # 만약 뒤에 수가 앞에 수보다 크면
            move += m-(num_list[i+1]-num_list[i])-1  # M - (n_2 - n_1) - 1
        for j in range(len(num_list)):  # 리스트 조사
            if num_list[j] > num_list[i]:  # 만약 j번째 리스트 수가 i보다 크다면
                num_list[j] -= 1  # 1 감소
    else:
        if num_list[i] > num_list[i+1]: # 만약 앞에 수가 뒤에 수보다 크면
            move += (num_list[i]-num_list[i+1]) # n_1 - n_2
        else:   # 만약 뒤에 수가 앞에 수보다 크면
            move += (num_list[i+1]-num_list[i])  # n_2 - n_1
        for j in range(len(num_list)):  # 리스트 조사
            if num_list[j] > num_list[i]:  # 만약 j번째 리스트 수가 i보다 크다면
                num_list[j] -= 1  # 1 감소
    m -= 1 # 원형큐 크기 감소

print(move)
