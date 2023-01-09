while True: # 무한루프
    try: #Error 안나면
        length = int(input()) #길이 받아오기
        price_line = input() #주가 라인 받아오기
        pricing = " ".join(price_line.split()) # 주가 나누어주기
        price_list = list(map(int, pricing.split())) # 나눈 주가를 정수로 바꿔주기
        line_list = [] # 검증 리스트 생성

        for i in range(length): # 반복문
            num = price_list.pop(0) # 주가 리스트의 맨 처음 주가 가져오기
            if i + 1 == length: # 만약 i+1가 주가 길이보다 길면
                break #멈추기
            if i == 0: #만약 i == 0
                line_list.append(num) #검증 리스트에 num 추가
            elif num > line_list[-1]: # num이 검증리스트 맨 뒷 주가보다 크면
                line_list.append(num) # 검증리스트에 num을 추가
            else: # num이 검증리스트 맨 뒷 주가보다 작으면
                line_list[-1] = num # 검증리스트의 맨 뒷 주가를 num으로 업데이트

        print(len(line_list)) # 검증리스트의 길이를 출력

    except: # Error가 나면
        break # 멈춘다