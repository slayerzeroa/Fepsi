import sys

def knapsack(M, V, C, n):  # M: 배낭의 무게한도, V: 각 물건의 무게, C: 각 물건의 만족도, n: 보석의 수, A: 중복되는 개수
    K = [[0 for x in range(M+1)] for x in range(n+1)]  # DP 2차원 리스트 생성
    for i in range(n+1):      # 행
        for m in range(M+1):  # 열
            if i==0 or m==0:  # 만약 0번째 행과 열 0으로 설정
                K[i][m] = 0
            elif V[i-1] <= m: # 만약 물건의 무게가 배낭의 무게한도보다 작으면
                K[i][m] = max(C[i-1]+K[i-1][m-V[i-1]], K[i-1][m])  # max함수를 이용해 비교해서 넣어준다
            else:       # 만약 물건의 무게가 배낭의 무게한도보다 크면
                K[i][m] = K[i-1][m] # 뒤에 있는 것을 그대로 넣어준다
    return K[n][M]  # DP 리턴

C = []      # 물건의 만족도
V = []      # 각 물건의 무게
N, M = map(int, sys.stdin.readline().strip().split())  # N = 물건의 종류의 수  M = 가방의 무게한도
for i in range(N):      # 물건의 종류 수만큼 반복
    v, c, a = map(int, sys.stdin.readline().strip().split())  # v = 물건 무게, c = 만족도, a = 물건의 개수
    for j in range(a):  # 물건의 개수만큼 반복
        if a <= 0:      # 만약 a<=0이면
            break       # 멈춰!
        else:           # 아니면
            tmp = min(2**j, a)  # 이진수로 중복을 방지함
            C.append(c*tmp)     # C에 tmp만큼의 만족도를 넣는다
            V.append(v*tmp)     # V에 tmp만큼의 물건 무게를 넣는다
            a -= tmp            # a -= tmp

print(knapsack(M, V, C, len(V)))  # 배낭문제 해결