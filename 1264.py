vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']      # 모음 리스트

check_num = []          # check_num list 생성

while True:             # 무한루프
    sentence = list(input())    # 문장 = 입력값의 리스트
    if sentence[0] == '#':      # 만약 문장이 # 하나로 이루어져 있으면
        break                   # 무한루프 탈출
    num = 0                     # num = 0 설정
    for i in sentence:          # sentence 원소 꺼내기
        if i in vowel:          # 만약 sentence 원소가 모음 리스트에 포함되어 있으면
            num += 1            # num + 1 하기
    check_num.append(num)       # num을 check_num 리스트에 추가

for i in check_num:             # check_num 리스트 원소 출력
    print(i)