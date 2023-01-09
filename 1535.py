iterate = int(input())          # 반복횟수 받아오기

life_steal = list(map(int, input().split()))    # 생명 감소 리스트
happiness = list(map(int, input().split()))     # 행복 증가 리스트

check_list=[]           # 체크 리스트 생성
for i in range(iterate):    # 2차원 배열로 만들어주기 (dic 형태 처럼)
    check_list.append([life_steal[i], happiness[i]])
check_list.sort(key=lambda x : (x[0], -x[1]))   # 0번째 열을 기준으로 오름차순, 1번째 열을 기준으로 내림차순 정렬

dp = [[0 for x in range(101)] for x in range(iterate)]  # 다이나믹 프로그래밍 2차원 리스트 생성

for i in range(iterate):        # 모든 다이나믹 리스트 방문
    for j in range(1, 101):
        if check_list[i][0] < j:    # 만약 생명 감소량보다 j가 크면
            dp[i][j] = max(check_list[i][1]+dp[i-1][j-check_list[i][0]], dp[i-1][j])    # max 함수로 비교해주기
        else:   # 만약 생명 감소량이 j보다 크면
            dp[i][j] = dp[i-1][j]   # 뒤에 있는거 그대로 가져오기

print(dp[iterate][-1])