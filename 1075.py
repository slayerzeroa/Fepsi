Dividend = list(input())        # 나눠지는 수 (피제수)
Divisor = int(input())          # 나누는 수 (제수)

Dividend[-1] = '0'              # 피제수 뒤 두 자리 00으로 변경
Dividend[-2] = '0'

Dividend = int(''.join(Dividend))   # 피제수 정수형으로 변경

while Dividend % Divisor != 0:      # 피제수를 제수로 나누었을 때 딱 떨어질 때까지 반복
    Dividend+=1                     # 피제수 +1

Dividend_list = list(map(int, str(Dividend)))   # 각 자리수를 리스트에 저장
print(str(Dividend_list[-2])+str(Dividend_list[-1]))    # 문자형으로 변경 후 뒤 두자리 출력