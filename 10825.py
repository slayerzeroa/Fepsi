iterate = int(input())          # 반복횟수

data = []       # 2차원 배열

for i in range(iterate):        # 반복횟수만큼 반복
    a = input().split()         # 나눠주기
    a[1] = int(a[1])            # 수치는 수치로 변경
    a[2] = int(a[2])
    a[3] = int(a[3])
    data.append(a)              # 데이터 리스트에 넣어줌 (데이터 리스트는 2차원 배열0)

data.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))         # 정렬 해주기

for i in range(len(data)):          # 데이터 길이만큼 반복해주기
    print(data[i][0])               # 이름 출력
