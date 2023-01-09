scale, jump = map(int, input().split()) # 인풋 받아오기
num_list = []       # 리스트 생성
result = []         # 결과 리스트 생성
index = 0           # 인덱스 값

for i in range(scale):  # scale만큼 반복하기
    num_list.append(i+1)    # 리스트 원소 생성

for i in range(scale):  # scale만큼 반복하기
    index += jump-1     # 인덱스 값에 jump-1 값을 더한다
    if index >= len(num_list):  # 만약 index가 num_list의 길이보다 길거나 같으면
        index %= len(num_list)  # 인덱스를 num_list의 길이로 나눈 나머지 값으로 업데이트
    result.append(num_list.pop(index))  # 결과 리스트에 num_list 인덱스 값을 추가

result = list(map(str, result)) # 문자열로 변환
result = '<' + ', '.join(result) + '>'  # 결과 폼 만들어주기

print(result)   # 결과 출력