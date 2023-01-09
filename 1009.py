iterate = int(input())

for i in range(iterate):
    case = input().split()
    if case[0][-1] == '1':
        print(1)
    if case[0][-1] == '5':
        print(5)
    if case[0][-1] == '6':
        print(6)
    if case[0][-1] == '0':
        print(10)
    if case[0][-1] == '2':
        if int(case[1]) % 4 == 1:
            print(2)
        if int(case[1]) % 4 == 2:
            print(4)
        if int(case[1]) % 4 == 3:
            print(8)
        if int(case[1]) % 4 == 0:
            print(6)
    if case[0][-1] == '3':
        if int(case[1]) % 4 == 1:
            print(3)
        if int(case[1]) % 4 == 2:
            print(9)
        if int(case[1]) % 4 == 3:
            print(7)
        if int(case[1]) % 4 == 0:
            print(1)
    if case[0][-1] == '4':
        if int(case[1]) % 4 == 1:
            print(4)
        if int(case[1]) % 4 == 2:
            print(6)
        if int(case[1]) % 4 == 3:
            print(4)
        if int(case[1]) % 4 == 0:
            print(6)
    if case[0][-1] == '7':
        if int(case[1]) % 4 == 1:
            print(7)
        if int(case[1]) % 4 == 2:
            print(9)
        if int(case[1]) % 4 == 3:
            print(3)
        if int(case[1]) % 4 == 0:
            print(1)

    if case[0][-1] == '8':
        if int(case[1]) % 4 == 1:
            print(8)
        if int(case[1]) % 4 == 2:
            print(4)
        if int(case[1]) % 4 == 3:
            print(2)
        if int(case[1]) % 4 == 0:
            print(6)

    if case[0][-1] == '9':
        if int(case[1]) % 4 == 1:
            print(9)
        if int(case[1]) % 4 == 2:
            print(1)
        if int(case[1]) % 4 == 3:
            print(9)
        if int(case[1]) % 4 == 0:
            print(1)

