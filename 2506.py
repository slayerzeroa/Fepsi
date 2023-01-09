N = int(input())        # length
score_list = list(map(int, input().split()))    # 점수 리스트 받아오기
score = 0           # 점수 최초 설정
check = 1           # check 최초 설정
for i in range(N):  # N만큼 반복
    if i+1 == len(score_list):  # 만약 score_list 마지막 원소이고
        if score_list[i] == 1:  # 만약 score_list 마지막 원소가 1이면
            score += check      # score에 check 수 더하기
        else:                   # 아니면
            score += 0          # 넘겨
    else:                       # 만약 score_list 진행 중이고
        if score_list[i] == 1 and score_list[i+1] == 1: # score_list가 연속으로 1이 나오면
            score += check      # score에 check를 더하고
            check += 1          # check +=1 해준다
        elif score_list[i] == 1 and score_list[i+1] == 0:   # 만약 i번째는 1이고 i+1번째는 0이면
            score += check      # score에 check를 더해준다
        else:                   # 만약 i번째가 0이면
            check = 1           # check는 초기화
            score += 0
print(score)    # 점수 출력