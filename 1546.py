iteration = int(input())        # 반복 횟수 설정

score = list(map(int, input().split()))     # 점수 입력 받기

high_score = max(score) # 최고점수 구해주기

for i in range(len(score)):     # score 길이만큼 반복
    score[i] = score[i]/high_score*100  # score 업데이트


total_score = 0
for i in range(len(score)):
    total_score += score[i]

print(total_score/len(score))