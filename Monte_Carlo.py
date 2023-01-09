def simulate_gbm(sigma, ITERATION, TIME_STEP, random_seed=42):  # 기하브라운운동 몬테카를로 시뮬레이션
    np.random.seed(random_seed)  # 랜덤으로 seed 뿌리고
    W = stats.norm.ppf(np.random.rand(ITERATION, TIME_STEP))  # 누적분포함수 역함수
    sheet = np.zeros(shape=[ITERATION, TIME_STEP + 1])  # 행렬 생성
    for i in range(ITERATION):
        sheet[i, 0] = STOCK_PRICE
        for j in range(1, TIME_STEP + 1):
            sheet[i, j] = sheet[i, j - 1] * np.exp((rf - 0.5 * sigma ** 2) + sigma * W[i, j - 1])
    return sheet