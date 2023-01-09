iterate = int(input())

correct = 0

for i in range(iterate):                # 반복횟수만큼 반복
    word_list = list(input())           # 단어의 스펠링 리스트 생성

    if len(word_list) == 1:             # 만약 단어의 길이가 1이면
        correct += 1                    # 적중
    else:                               # 만약 단어의 길이가 1이 아니면
        word_check_list = []            # 단어 체크 리스트 생성
        for j in range(len(word_list)):     # (word_list 스펠링 개수 - 1)만큼 반복
            word_check_list.append(word_list.pop()) # word list에서 pop한 단어를 word check list에 저장
            if len(word_list) == 0:
                correct += 1
                break
            if word_check_list[0] == word_list[-1]:# 만약 check word와 word_list 마지막 단어가 같으면
                continue
            else:                                   # 같지 않고
                if word_check_list[0] in word_list: # check word가 word list 안에 있으면
                    break   # 반복문 종료
                word_check_list.clear()

print(correct)