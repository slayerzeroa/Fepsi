x = int(input())    # 위치 받아오기

dp = [0]*5002       # dynamic programming 리스트 생성

for i in range(3, 5002):        # 반복
    if i % 15 == 0:             # 만약 i가 15로 나누어 떨어지면
        dp[i] = min(dp[i-5]+1, dp[i-3]+1)   # 비교
    elif i % 5 == 0:    # 5로 나누어 떨어지면
        dp[i] = dp[i-5]+1   # +1
    elif i % 3 == 0:    # 3으로 나누어 떨어지면
        dp[i] = dp[i-3]+1   # +1
    elif i == 8:        # 만약 i가 8이면
        dp[i] = 2       # 손수 채워주기
    elif i > 10:        # i가 10 이상이면 무조건 됨
        dp[i] = dp[i-3]+1   # i-3 위치 값에 +1

#print(dp)
if dp[x] == 0:  # 만약 dp[0]이 0이면
    print(-1)   # -1 출력
else:           # 아니면
    print(dp[x])# 그냥 출력~