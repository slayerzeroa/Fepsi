# N번째 큰 수 -> sort 쉬움

iterate = int(input())  # 반복횟수
index = 3               # 인덱스 설정

for i in range(iterate):    # 반복횟수만큼 반복
    num_list = list(map(int, input().split()))  # 숫자 배열 받기
    num_list.sort(reverse=True)                 # 내림차순 정렬
    print(num_list[index-1])                    # 결과값 출력