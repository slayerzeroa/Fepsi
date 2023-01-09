num_list = list(input())        # 인풋 받아오기
num_list_5 = list(num_list)     # 5가 6으로 바뀌는 경우
num_list_6 = list(num_list)     # 6이 5로 바뀌는 경우

for i in range(len(num_list_5)):        # num_list_5 길이만큼 반복
    if num_list_5[i] == '5':            # 만약 5면
        num_list_5[i] = '6'             # 6으로 변경

for i in range(len(num_list_6)):        # num_list_6 길이만큼 반복
    if num_list_6[i] == '6':            # 만약 6이면
        num_list_6[i] = '5'             # 5로 변경


result_5 = list(map(int, ''.join(num_list_5).split()))      # 결과값
result_6 = list(map(int, ''.join(num_list_6).split()))      # 결과값

print(result_6[0] + result_6[1], result_5[0] + result_5[1])     # 결과값