status = input().split()        # 상태 받아오기 (큐의 크기, 뽑아내려는 수의 개수)
m = int(status[0])              # 큐의 크기
iterate = int(status[1])        # 뽑아내려는 수의 개수

num_list = input().split()      # 뽑아내려는 수의 위치
move = 0                        # 총 움직인 횟수
num_list = list(map(int,num_list))  # 리스트 int형으로 바꿔주기

queue = []          # queue 만들어주기


for i in range(m):      # 큐의 크기만큼
    queue.append(i+1)   # 큐 원소 넣어주기

queue_left = list(queue)  # left queue 생성
queue_right = list(queue) # right queue 생성


def turn_left(queue):        # 좌회전
    queue.append(queue[0])
    del queue[0]
    return queue

def turn_right(queue):       # 우회전
    queue.insert(0, queue[-1])
    queue.pop()
    return queue

for i in range(iterate):   # 반복횟수만큼 반복
    left_num = 0    # 왼쪽으로 간 횟수
    right_num = 0   # 오른쪽으로 간 횟수

    while queue_left[0] != num_list[i]:  # while문
        turn_left(queue_left)   # 돌려주기
        left_num += 1   # 돌린 횟수 저장

    while queue_right[0] != num_list[i]:  # while문
        turn_right(queue_right)   # 돌려주기
        right_num += 1   # 돌린 횟수 저장

    if left_num > right_num:    # 만약 왼쪽으로 돌린 횟수가 오른쪽으로 돌린 횟수보다 크면
        move += right_num       # 움직인 횟수에 우회전 횟수 더하기
    else:                       # 아니면
        move += left_num        # 움직인 횟수에 좌회전 횟수 더하기

    del queue_right[0]          # 첫번째 원소 삭제

    queue = list(queue_right)   # 큐 초기화
    queue_left = list(queue)    # 좌회전 큐 초기화

print(move) # 총 움직인 횟수 출력