# 백준 1231번; 주식왕 동호 정답지
stock_num, time, money = map(int, input().split()) # 인풋 받아오기

total_stock = [] # 빈 리스트 만들어주기

for i in range(stock_num): # 다음 데이터 모두 받아오기
    total_stock.append(list(map(int, input().split()))) # 맵 함수 예제 참고

for i in range(time): # 계산식
    profit_list = [] # 빈 리스트 생성
    if i + 1 == time: # 만약 인덱스가 초과되면
        break # 멈추기
    else: #아니면 계산 ㄱㄱ
        for j in range(stock_num): # 주식 수만큼 반복
            if money >= total_stock[j][i]: # 만약 현재 머니가 주가보다 많거나 같다면
                num = money // total_stock[j][i]
                profit = num*(total_stock[j][i+1] - total_stock[j][i]) # 1 간극간 수익 계산
            else: # 아니면
                profit = 0 # 수익 0원
            profit_list.append(profit) #수익 추가해주기
        money += max(profit_list)
print(money) # 출력

