scale, jump = map(int, input().split()) # 인풋 받아오기
num_list = []       # 원형 리스트 생성
result_list = []    # 결과 리스트 생성

for i in range(scale):  # scale만큼 반복하기
    num_list.append(i+1)    # 원형 리스트 원소 생성

def turn():                 # 돌리기 함수
    num_list.append(num_list[0])
    del num_list[0]

while num_list != []:       # num_list가 비어있을 때까지
    for i in range(jump-1): # 2번씩 돌리기 (n번째 원소에 도달하기 까지 n-1 회전 필요)
        turn()              # 회전

    result_list.append(num_list[0])     # 회전 리스트의 0번째 원소를 결과 리스트에 추가
    del num_list[0]                     # 원소 삭제

result_list = list(map(str, result_list))

result = ', '.join(result_list)
result = '<' + result + '>'

print(result)