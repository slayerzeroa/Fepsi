# sort 정리 문제 리스트 A의 가장 작은 수를 리스트 B의 가장 큰 수에 곱하면서 올라가면 됨

q = input() # 길이 받아주기

A_list = input().split()    # A_list 생성
B_list = input().split()    # B_list 생성

A_list = list(map(int,A_list))  # A_list int형으로 변경
B_list = list(map(int,B_list))  # B_list int형으로 변경

A_list.sort()                   # A_list 오름차순 정렬
B_list.sort(reverse=True)       # B_list 내림차순 정렬

result = 0                      # 결과값 생성

for i in range(len(A_list)):    # 길이만큼 반복
    multi = int(A_list[i]) * int(B_list[i]) # A_list의 가장 작은 수와 B_list의 가장 큰 수 곱해주기
    result += multi # 결과값에 더해주기

print(result)   # 결과값 출력