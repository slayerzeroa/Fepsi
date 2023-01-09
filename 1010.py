iterate = int(input())  # 반복횟수 받아오기

# 조합 문제 mCn

for i in range(iterate):    # 반복횟수만큼 반복
    num_list = input().split()  # 사이트 개수 받아오기
    m = int(num_list[1])        # 서쪽 사이트 개수
    n = int(num_list[0])        # 동쪽 사이트 개수
    a = m-n                     # (m-n)! 구하기 위해서
    m_result = 1                # m 결과값 초기설정
    n_result = 1                # n 결과값 초기설정
    a_result = 1                # a 결과값 초기설정
    for j in range(1, m+1):     # m!
        m_result*=j

    for k in range(1, n+1):     # n!
        n_result*=k

    for u in range(1, a+1):     # (m-n)!
        a_result*=u

    print(m_result//(n_result*a_result))    #m!/(n!(m-n)!)
