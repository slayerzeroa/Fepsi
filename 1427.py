num = input()                           # 입력 받기
num_list = list(num)                    # 리스트로 변환
num_list = list(map(int, num_list))     # 정수형으로 변환
num_list.sort(reverse=True)             # 내림차순으로 정렬
num_list = list(map(str, num_list))     # 문자열로 변경

result = ''.join(num_list)              # 문자열로 변경
print(result)                           # 결과값 출력