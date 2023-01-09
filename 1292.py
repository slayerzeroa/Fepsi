interval = list(map(int, input().split()))  # 구간 받아오기

num_list = []       # 숫자 리스트 생성

for i in range(100):    # 100까지 반복
    for j in range(i):      # 이중 포문
        num_list.append(i)  # 조건에 맞는 리스트 생성하기

num_list = num_list[interval[0]-1:interval[1]]  # 구간에 맞게 인덱싱

print(sum(num_list))    # 인덱싱 한 합을 출력