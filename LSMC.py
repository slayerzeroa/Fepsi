'''
Author : slayerzeroa(유대명)

It was created to teach in FEPSI.

Reference : Longstaff & Schwartz

LSMC MODEL
: SIMPLE
'''

import os

import pandas as pd
import numpy as np
import math
import timeit
import csv
import scipy.stats as stats


STOCK_PRICE = 1000  # 주가
STRIKE_PRICE = 1200  # 행사가

STRIKE_ORG = 0  # 변동되는 행사가격 (변수)
Type = 'Call'    # Choose 'Call' or 'Put'
sigma = 0.06        # 변동성   일일 단위 주의
TIME_STEP = 300       # 일일 단위 주의
rf = 0.003          # 일일 단위 주의
ITERATION = 10000  # 시행 횟수

#vesting = int(df.iloc[153, 7])  # 가득기간

# occur_price = int(df.iloc[1, 25]) # 시가조정리픽싱 발생 가격
# STRIKE_PRICE_REFIX = int(df.iloc[2, 25]) # 시가조정리픽싱 행사가격

if (Type == 'Call') == True:  # 만약 옵션 타입이 단순 American이면
    start = timeit.default_timer()


    ## Simple Model
    # Step 0 : Monte Carlo Simulation

    def simulate_gbm(sigma, ITERATION, TIME_STEP, random_seed=42):  # 기하브라운운동 몬테카를로 시뮬레이션
        np.random.seed(random_seed)  # 랜덤으로 seed 뿌리고
        W = stats.norm.ppf(np.random.rand(ITERATION, TIME_STEP))  # 누적분포함수 역함수
        sheet = np.zeros(shape=[ITERATION, TIME_STEP + 1])  # 행렬 생성
        for i in range(ITERATION):
            sheet[i, 0] = STOCK_PRICE
            for j in range(1, TIME_STEP + 1):
                sheet[i, j] = sheet[i, j - 1] * np.exp((rf - 0.5 * sigma ** 2) + sigma * W[i, j - 1])
        return sheet


    gbm = simulate_gbm(sigma, ITERATION, TIME_STEP)  # 기하 브라운 운동
    gbm = pd.DataFrame(gbm)
    print(gbm)

    ### Step 1 : stock price path by Monte Carlo simulation
    gbm = gbm.values

    ### Step 2 : generate ITM stock price path
    start_cond = timeit.default_timer()
    ITM = gbm  # ITM DataFrame 생성

    for i in range(gbm.shape[0]):  # 행만큼 반복
        for j in range(gbm.shape[1]):  # 열만큼 반복
            if ITM[i, j] < STRIKE_PRICE:  # 만약 gbm 가격이 행사가격보다 작으면 # Call
                ITM[i, j] = 0  # Null 추가
    end_cond = timeit.default_timer()
    print(f"ITM 확인시간은{end_cond - start_cond}")

    ### Step 3
    r_HV = np.zeros(shape=[gbm.shape[0], gbm.shape[1]])  # r-HV DataFrame 생성

    ### Step 4
    least_square = np.zeros(shape=[3, gbm.shape[1]])  # least_square DataFrame 생성

    ### Step 5
    Optimized = np.zeros(shape=[gbm.shape[0], gbm.shape[1]])  # Optimized DataFrame 생성

    ### Step 5-1
    payoff_option_price = np.zeros(shape=[gbm.shape[0], 1])

    start_cond = timeit.default_timer()
    for i in range(payoff_option_price.shape[0]):
        if ITM[i, TIME_STEP] == 0:  # ITM 마지막 열의 행마다 검증, 0이 있으면
            payoff_option_price[i, 0] = 0  # payoff_option에도 0 추가
        else:  # 아니면
            payoff_option_price[i, 0] = max(0, (ITM[i, TIME_STEP] - STRIKE_PRICE))  # 값 추가
    end_cond = timeit.default_timer()
    print(f"payoff 확인시간은{end_cond - start_cond}")


    ### 회귀분석 검증식
    def E_Y_X(a_0, a_1, a_2, X):
        result = a_0 + (a_1 * X) + (a_2 * (X ** 2))
        return result


    start_iteration = timeit.default_timer()
    for j in range(gbm.shape[1] - 1, -1, -1):  # 후행
        ### Step 3 : rolled back HV of ITM path
        # start_cond = timeit.default_timer()
        if j + 1 == gbm.shape[1]:  # 만약 끝 열이라면
            r_HV[:, j] = 0  # r_HV 끝 열은 전부 Null
        else:  # 아니면
            for i in range(gbm.shape[0]):  # 행 개수만큼 반복
                if ITM[i, j] == 0:  # 만약 해당 셀에 ITM이 비어있으면
                    r_HV[i, j] = 0  # r_HV도 Null
                else:  # 아니면
                    r_HV[i, j] = (np.exp(-rf)) * (Optimized[i, j + 1])  # Optimized에서 할인해온다
        # end_cond = timeit.default_timer()
        # print(f"rolled back HV 확인시간은{end_cond - start_cond}")

        ### Step 4 : Least-Square Parameter Caculation
        # start_cond = timeit.default_timer()
        if j + 1 == gbm.shape[1]:  # 만약 끝 열이라면
            pass
        else:
            test = np.zeros(shape=[gbm.shape[0], 2])  # parameter test DataFrame 생성
            for i in range(test.shape[0]):  # test 행 개수만큼 반복
                if ITM[i, j + 1] == 0:  # 만약 ITM 뒷 셀이 0이면
                    test[i, 0] = 0  # test 첫 번째 열은 0
                    test[i, 1] = ITM[i, j]  # test 두 번째 열은 ITM 열과 같다
                else:  # 아니면
                    if (ITM[i, j + 1] - STRIKE_PRICE) < 0:
                        test[i, 0] = 0  # test 첫 번째 열은 0
                        test[i, 1] = ITM[i, j]  # test 두 번째 열은 ITM 열과 같다
                    else:
                        test[i, 1] = ITM[i, j]  # test 두 번째 열은 ITM 열과 같다
                        if test[i, 1] == 0:
                            test[i, 0] = 0
                        else:
                            test[i, 0] = Optimized[i, j + 1] * np.exp(-rf)  # test 셀은 optimized 할인한 값

            sample_value = test.shape[0]  # 계산할 떄 필요한 행의 개수 생성
            degree_1 = 0
            for i in range(test.shape[0]):  # ∑주가
                degree_1_sum = test[i, 1]
                if degree_1_sum == 0:
                    sample_value -= 1  # sample value에 0값이 들어있는 행의 개수 빼주기
                degree_1 += degree_1_sum

            degree_2 = 0
            for i in range(test.shape[0]):  # ∑주가^2
                degree_2_sum = (test[i, 1]) ** 2
                degree_2 += degree_2_sum

            degree_3 = 0
            for i in range(test.shape[0]):  # ∑주가^3
                degree_3_sum = (test[i, 1]) ** 3
                degree_3 += degree_3_sum

            degree_4 = 0
            for i in range(test.shape[0]):  # ∑주가^4
                degree_4_sum = (test[i, 1]) ** 4
                degree_4 += degree_4_sum

            Y = 0
            for i in range(test.shape[0]):  # ∑(주가 - 행사값)
                Y_sum = test[i, 0]
                Y += Y_sum

            Y_X = 0
            for i in range(test.shape[0]):  # ∑((주가 - 행사값)*주가)
                Y_sum = test[i, 0]
                X_sum = test[i, 1]
                Y_X += Y_sum * X_sum

            Y_X2 = 0
            for i in range(test.shape[0]):  # ∑((주가 - 행사값)*주가^2)
                Y_sum = test[i, 0]
                X_sum = (test[i, 1]) ** 2
                Y_X2 += Y_sum * X_sum

            # aa 행렬 생성
            aa = np.array([[sample_value, degree_1, degree_2],
                           [degree_1, degree_2, degree_3],
                           [degree_2, degree_3, degree_4]])

            # ab 행렬
            ab = np.array([[Y],
                           [Y_X],
                           [Y_X2]])

            if j < 1:
                pass
            if np.all(aa == 0) == True:  # 만약 aa 행렬이 영행렬이면
                pass  # 넘기기
            else:
                params = np.linalg.solve(aa, ab)  # 비선형 회귀분석 parameter 값
                a_0 = params[0, 0]  # a0
                a_1 = params[1, 0]  # a1
                a_2 = params[2, 0]  # a2

            for i in range(len(least_square)):  # least_square 값 추가
                least_square[0, j] = params[0, 0]
                least_square[1, j] = params[1, 0]
                least_square[2, j] = params[2, 0]
        end_cond = timeit.default_timer()
        # print(f"최소자승법 확인시간은{end_cond - start_cond}")

        ### Step 5 : Optimized Option Value by comparing least squared HV and Exercise Value
        # start_cond = timeit.default_timer()
        if j + 1 == gbm.shape[1]:  # 만약 끝 열이라면
            Optimized[:, j] = payoff_option_price[:, 0]  # Optimized 마지막 열은 payoff와 같다
        else:  # 아니면
            for i in range(ITM.shape[0]):  # ITM만큼 반복해줘
                if ITM[i, j] == 0:
                    pass
                else:
                    lambda_HV = least_square[0, j] + (least_square[1, j] * gbm[i, j]) + (
                            least_square[2, j] * (gbm[i, j] ** 2))  # 변하는 람다 HV값

                    if lambda_HV > max(0, (
                            gbm[i, j] - STRIKE_PRICE)):  # 만약 lambda_HV가 gbm[i, j] - STRIKE PRICE ORG보다 크면
                        Optimized[i, j] = ((Optimized[i, j + 1]) * np.exp(-rf))  # Optimized 행렬에 할인된 값을 추가해준다
                    else:  # 아니면
                        if ITM[i, j] == 0:  # ITM[i, j]가 0이면
                            Optimized[i, j] = 0  # Optimized 행렬도 0이다
                        else:  # 아니면
                            Optimized[i, j] = max(ITM[i, j] - STRIKE_PRICE,
                                                  0)  # Optimized 행렬에는 ITM - STRIKE PRICE ORG 추가
        # end_cond = timeit.default_timer()
        # print(f"optimized 확인시간은{end_cond - start_cond}")
    end_iteration = timeit.default_timer()
    print(f"iteration 확인시간은{end_iteration - start_iteration}")

    Optimized[:, 0] = 0
    m, n = Optimized.shape[0], Optimized.shape[1]

    ### Step 6 : Finding Exercising point by forward path
    start_cond = timeit.default_timer()
    exer_point = np.zeros(shape=[m, n])  # 영행렬 생성
    for i in range(exer_point.shape[0]):  # exer_point 행만큼 반복
        for j in range(exer_point.shape[1]):  # j는 1부터 시작
            if np.any(exer_point[i, 0:j] == 1) == False:  # 행 전체에 1이 한번이라도 포함이 안되고
                if ITM[i, j] != 0:  # ITM값이 0이 아니고
                    if Optimized[i, j] == (
                            gbm[i, j] - STRIKE_PRICE):  # Optimized_n의 값이 gbm - Strike price org와 같다면
                        exer_point[i, j] = 1  # 1
                        break  # 멈춰

    end_cond = timeit.default_timer()
    print(f"exer point 확인시간은{end_cond - start_cond}")

    ### Step 7 : option pricing by straightforwatd path
    start_cond = timeit.default_timer()
    option_price = pd.DataFrame(np.zeros(shape=[gbm.shape[0], gbm.shape[1]]))
    for j in range(len(option_price.columns)):  # j는 1부터 시작
        for i in range(len(option_price)):
            if exer_point[i, j] == 1:  # exercising path에서 1이라면
                option_price.iloc[i, j] = Optimized[i, j]
    end_cond = timeit.default_timer()
    print(f"option pricing 확인시간은{end_cond - start_cond}")

    ### Step 8 : calculate option price
    start_cond = timeit.default_timer()
    CashFlow = option_price.drop([option_price.columns[0]], axis=1)  # CashFlow는 X의 0번째 열 drop

    columns = []  # columns 리스트 생성
    option_price_num = 0  # 옵션 가격
    nums = len(CashFlow)  # CashFlow 길이 구해주기
    for column in CashFlow:  # CashFlow의 열 반복
        columns.append(column)  # columns 리스트에 column 넣어주기
        pricing = CashFlow[(CashFlow[column] != 0)]  # pricing은 하나의 열에 0이 아닌 값들만 추출한 DataFrame
        for i in range(len(pricing)):  # pricing 길이만큼 반복
            discount = np.exp(-rf)  # 할인율 구해주기
            for j in range(column - 2, 0, -1):  # 반복
                discount = discount * np.exp(-rf)  # 전체 할인율 계산
            option_price_num += pricing.iloc[i, column - 1] * discount  # option price 할인해주기
            # print(option_price_num)
    option_price_num = option_price_num / nums  # oprtion price는 전체 값의 평균

    print('옵션가격은')
    print(option_price_num)
    print('※ EXCEL 내보내기 작업 중 입니다. 프로그램을 종료하지 말아주세요. ※')

if (Type == 'Put') == True:  # 만약 옵션 타입이 단순 American인 Put Option이라면
    start = timeit.default_timer()


    ## Simple Model
    # Step 0 : Monte Carlo Simulataion

    def simulate_gbm(sigma, ITERATION, T, TIME_STEP, random_seed=42):  # 기하브라운운동 몬테카를로 시뮬레이션
        np.random.seed(random_seed)  # 랜덤으로 seed 뿌리고
        W = stats.norm.ppf(np.random.rand(ITERATION, TIME_STEP))  # 누적분포함수 역함수
        sheet = np.zeros(shape=[ITERATION, TIME_STEP + 1])  # 행렬 생성
        for i in range(ITERATION):
            sheet[i, 0] = STOCK_PRICE
            for j in range(1, TIME_STEP + 1):
                sheet[i, j] = sheet[i, j - 1] * np.exp((rf - 0.5 * sigma ** 2) + sigma * W[i, j - 1])
        return sheet


    gbm = simulate_gbm(sigma, ITERATION, TIME_STEP)  # 기하 브라운 운동
    gbm = pd.DataFrame(gbm)
    print(gbm)

    ### Step 1 : stock price path by Monte Carlo simulation
    gbm = gbm.values

    ### Step 2 : generate ITM stock price path
    start_cond = timeit.default_timer()
    ITM = gbm  # ITM DataFrame 생성

    for i in range(gbm.shape[0]):  # 행만큼 반복
        for j in range(gbm.shape[1]):  # 열만큼 반복
            if ITM[i, j] > STRIKE_PRICE:  # 만약 gbm 가격이 행사가격보다 작으면 # Put
                ITM[i, j] = 0  # Null 추가
    end_cond = timeit.default_timer()
    print(f"ITM 확인시간은{end_cond - start_cond}")

    ### Step 3
    r_HV = np.zeros(shape=[gbm.shape[0], gbm.shape[1]])  # r-HV DataFrame 생성

    ### Step 4
    least_square = np.zeros(shape=[3, gbm.shape[1]])  # least_square DataFrame 생성

    ### Step 5
    Optimized = np.zeros(shape=[gbm.shape[0], gbm.shape[1]])  # Optimized DataFrame 생성

    ### Step 5-1
    payoff_option_price = np.zeros(shape=[gbm.shape[0], 1])

    start_cond = timeit.default_timer()
    for i in range(payoff_option_price.shape[0]):
        if ITM[i, TIME_STEP] == 0:  # ITM 마지막 열의 행마다 검증, 0이 있으면
            payoff_option_price[i, 0] = 0  # payoff_option에도 0 추가
        else:  # 아니면
            payoff_option_price[i, 0] = max(0, -(ITM[i, TIME_STEP] - STRIKE_PRICE))  # 값 추가 #Put
    end_cond = timeit.default_timer()
    print(f"payoff 확인시간은{end_cond - start_cond}")


    ### 회귀분석 검증식
    def E_Y_X(a_0, a_1, a_2, X):
        result = a_0 + (a_1 * X) + (a_2 * (X ** 2))
        return result


    start_iteration = timeit.default_timer()
    for j in range(gbm.shape[1] - 1, -1, -1):  # 후행
        ### Step 3 : rolled back HV of ITM path
        # start_cond = timeit.default_timer()
        if j + 1 == gbm.shape[1]:  # 만약 끝 열이라면
            r_HV[:, j] = 0  # r_HV 끝 열은 전부 Null
        else:  # 아니면
            for i in range(gbm.shape[0]):  # 행 개수만큼 반복
                if ITM[i, j] == 0:  # 만약 해당 셀에 ITM이 비어있으면
                    r_HV[i, j] = 0  # r_HV도 Null
                else:  # 아니면
                    r_HV[i, j] = (np.exp(-rf)) * (Optimized[i, j + 1])  # Optimized에서 할인해온다
        # end_cond = timeit.default_timer()
        # print(f"rolled back HV 확인시간은{end_cond - start_cond}")

        ### Step 4 : Least-Square Parameter Caculation
        # start_cond = timeit.default_timer()
        if j + 1 == gbm.shape[1]:  # 만약 끝 열이라면
            pass
        else:
            test = np.zeros(shape=[gbm.shape[0], 2])  # parameter test DataFrame 생성
            for i in range(test.shape[0]):  # test 행 개수만큼 반복
                if ITM[i, j + 1] == 0:  # 만약 ITM 뒷 셀이 0이면
                    test[i, 0] = 0  # test 첫 번째 열은 0
                    test[i, 1] = ITM[i, j]  # test 두 번째 열은 ITM 열과 같다
                else:  # 아니면
                    if -(ITM[i, j + 1] - STRIKE_PRICE) < 0:  # Put
                        test[i, 0] = 0  # test 첫 번째 열은 0
                        test[i, 1] = ITM[i, j]  # test 두 번째 열은 ITM 열과 같다
                    else:
                        test[i, 1] = ITM[i, j]  # test 두 번째 열은 ITM 열과 같다
                        if test[i, 1] == 0:
                            test[i, 0] = 0
                        else:
                            test[i, 0] = Optimized[i, j + 1] * np.exp(-rf)  # test 셀은 optimized 할인한 값

            sample_value = test.shape[0]  # 계산할 떄 필요한 행의 개수 생성
            degree_1 = 0
            for i in range(test.shape[0]):  # ∑주가
                degree_1_sum = test[i, 1]
                if degree_1_sum == 0:
                    sample_value -= 1  # sample value에 0값이 들어있는 행의 개수 빼주기
                degree_1 += degree_1_sum

            degree_2 = 0
            for i in range(test.shape[0]):  # ∑주가^2
                degree_2_sum = (test[i, 1]) ** 2
                degree_2 += degree_2_sum

            degree_3 = 0
            for i in range(test.shape[0]):  # ∑주가^3
                degree_3_sum = (test[i, 1]) ** 3
                degree_3 += degree_3_sum

            degree_4 = 0
            for i in range(test.shape[0]):  # ∑주가^4
                degree_4_sum = (test[i, 1]) ** 4
                degree_4 += degree_4_sum

            Y = 0
            for i in range(test.shape[0]):  # ∑(주가 - 행사값)
                Y_sum = test[i, 0]
                Y += Y_sum

            Y_X = 0
            for i in range(test.shape[0]):  # ∑((주가 - 행사값)*주가)
                Y_sum = test[i, 0]
                X_sum = test[i, 1]
                Y_X += Y_sum * X_sum

            Y_X2 = 0
            for i in range(test.shape[0]):  # ∑((주가 - 행사값)*주가^2)
                Y_sum = test[i, 0]
                X_sum = (test[i, 1]) ** 2
                Y_X2 += Y_sum * X_sum

            # aa 행렬 생성
            aa = np.array([[sample_value, degree_1, degree_2],
                           [degree_1, degree_2, degree_3],
                           [degree_2, degree_3, degree_4]])

            # ab 행렬
            ab = np.array([[Y],
                           [Y_X],
                           [Y_X2]])

            if j < 1:
                pass
            if np.all(aa == 0) == True:  # 만약 aa 행렬이 영행렬이면
                pass  # 넘기기
            else:
                params = np.linalg.solve(aa, ab)  # 비선형 회귀분석 parameter 값
                a_0 = params[0, 0]  # a0
                a_1 = params[1, 0]  # a1
                a_2 = params[2, 0]  # a2

            for i in range(len(least_square)):  # least_square 값 추가
                least_square[0, j] = params[0, 0]
                least_square[1, j] = params[1, 0]
                least_square[2, j] = params[2, 0]
        end_cond = timeit.default_timer()
        # print(f"최소자승법 확인시간은{end_cond - start_cond}")

        ### Step 5 : Optimized Option Value by comparing least squared HV and Exercise Value
        # start_cond = timeit.default_timer()
        if j + 1 == gbm.shape[1]:  # 만약 끝 열이라면
            Optimized[:, j] = payoff_option_price[:, 0]  # Optimized 마지막 열은 payoff와 같다
        else:  # 아니면
            for i in range(ITM.shape[0]):  # ITM만큼 반복해줘
                if ITM[i, j] == 0:
                    pass
                else:
                    lambda_HV = least_square[0, j] + (least_square[1, j] * gbm[i, j]) + (
                            least_square[2, j] * (gbm[i, j] ** 2))  # 변하는 람다 HV값

                    if lambda_HV > max(0, -(
                            gbm[i, j] - STRIKE_PRICE)):  # 만약 lambda_HV가 -(gbm[i, j] - STRIKE PRICE ORG)보다 크면 # Put
                        Optimized[i, j] = ((Optimized[i, j + 1]) * np.exp(-rf))  # Optimized 행렬에 할인된 값을 추가해준다
                    else:  # 아니면
                        if ITM[i, j] == 0:  # ITM[i, j]가 0이면
                            Optimized[i, j] = 0  # Optimized 행렬도 0이다
                        else:  # 아니면
                            Optimized[i, j] = max(-(ITM[i, j] - STRIKE_PRICE),
                                                  0)  # Optimized 행렬에는 -(ITM - STRIKE PRICE ORG) 추가 Put
        # end_cond = timeit.default_timer()
        # print(f"optimized 확인시간은{end_cond - start_cond}")

    end_iteration = timeit.default_timer()
    print(f"iteration 확인시간은{end_iteration - start_iteration}")
    Optimized[:, 0] = 0
    m, n = Optimized.shape[0], Optimized.shape[1]

    ### Step 6 : Finding Exercising point by forward path
    start_cond = timeit.default_timer()
    exer_point = np.zeros(shape=[m, n])  # 영행렬 생성
    for i in range(exer_point.shape[0]):  # exer_point 행만큼 반복
        for j in range(exer_point.shape[1]):  # j는 1부터 시작
            if np.any(exer_point[i, 0:j] == 1) == False:  # 행 전체에 1이 한번이라도 포함이 안되고
                if ITM[i, j] != 0:  # ITM값이 0이 아니고
                    if Optimized[i, j] == (-(
                            gbm[i, j] - STRIKE_PRICE)):  # Optimized_n의 값이 -(gbm - Strike price org)와 같다면
                        exer_point[i, j] = 1  # 1
                        break  # 멈춰

    end_cond = timeit.default_timer()
    print(f"exer point 확인시간은{end_cond - start_cond}")

    ### Step 7 : option pricing by straightforwatd path
    start_cond = timeit.default_timer()
    option_price = pd.DataFrame(np.zeros(shape=[gbm.shape[0], gbm.shape[1]]))
    for j in range(len(option_price.columns)):  # j는 1부터 시작
        for i in range(len(option_price)):
            if exer_point[i, j] == 1:  # exercising path에서 1이라면
                option_price.iloc[i, j] = Optimized[i, j]
    end_cond = timeit.default_timer()
    print(f"option pricing 확인시간은{end_cond - start_cond}")

    ### Step 8 : calculate option price
    start_cond = timeit.default_timer()
    CashFlow = option_price.drop([option_price.columns[0]], axis=1)  # CashFlow는 X의 0번째 열 drop

    columns = []  # columns 리스트 생성
    option_price_num = 0  # 옵션 가격
    nums = len(CashFlow)  # CashFlow 길이 구해주기
    for column in CashFlow:  # CashFlow의 열 반복
        columns.append(column)  # columns 리스트에 column 넣어주기
        pricing = CashFlow[(CashFlow[column] != 0)]  # pricing은 하나의 열에 0이 아닌 값들만 추출한 DataFrame
        for i in range(len(pricing)):  # pricing 길이만큼 반복
            discount = np.exp(-rf)  # 할인율 구해주기
            for j in range(column - 2, 0, -1):  # 반복
                discount = discount * np.exp(-rf)  # 전체 할인율 계산
            option_price_num += pricing.iloc[i, column - 1] * discount  # option price 할인해주기
            # print(option_price_num)
    option_price_num = option_price_num / nums  # oprtion price는 전체 값의 평균

    end_cond = timeit.default_timer()
    print(f"calculate option price 확인시간은{end_cond - start_cond}")

    print('옵션가격은')
    print(option_price_num)