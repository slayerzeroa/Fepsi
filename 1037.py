a = input() # input

num_list = list(map(int, input().split()))  # num_list 받아오기
num_list.sort() # 오름차순 정렬

result = num_list[0] * num_list[-1] # 맨 앞 원소와 맨 뒤 원소를 곱해준다
print(result)           # 결과값 출력