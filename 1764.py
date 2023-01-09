a, b = map(int, input().split())     # 초기값 입력

a_set = set([])         # a_set 생성
b_set = set([])         # b_set 생성
result_list = []        # 결과 리스트 생성

for i in range(a):      # a만큼 반복
    a_set.add(input())  # a_set에 원소 추가

for i in range(b):      # b만큼 반복
    b_set.add(input())  # b_set에 원소 추가

result_set = a_set & b_set  # 결과 셋

result_list = list(result_set)  # 리스트 변환

result_list.sort()          # 정렬(오름차순)
print(len(result_list))     # result_list 길이 출력
for i in result_list:       # result_list 원소 출력
    print(i)