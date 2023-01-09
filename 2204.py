while True:                                     # 무한루프
    N = int(input())                            # 반복횟수 받아주기
    if N == 0:                                  # 만약 N이 0이면
        break                                   # 무한루프
    check_list = []                             # 체크리스트 생성
    for _ in range(N):                          # 반복횟수만큼 반복
        word = input()                          # 단어 받아주기
        upper_word = word.upper()               # 대문자로 변경된 단어
        check_list.append([upper_word, word])   # 2차원 배열로 저장
    check_list.sort(key = lambda x : x[0])      # 0번째 기준으로 정렬
    print(check_list[0][1])                     # 원하는 결과 출력
