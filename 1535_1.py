iterate = int(input())          # 반복횟수 받아오기

life_steal = list(map(int, input().split()))    # 생명 감소 리스트
happiness = list(map(int, input().split()))     # 행복 증가 리스트

life_steal = [0] + life_steal
happiness = [0] + happiness

dp = [[0 for _ in range(101)] for _ in range(iterate+1)]

for i in range(1, iterate+1):
    for j in range(1, 101):
        if life_steal[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-life_steal[i]] + happiness[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[iterate][99])