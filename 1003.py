a = int(input())

# fib_list = []       # 피보나치 수열 리스트

def fibonacci(num):         # 피보나치 재귀함수 # 시간초과;;
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

'''
for i in range(a):
    fib_list.clear()
    iterate = int(input())
    fibonacci(iterate)
    print(fib_list)
    print(fib_list.count(0), fib_list.count(1))
'''


def fib(n):                     # 일반 함수로 짠 피보나치 수열 (시간 효율성 재귀함수 대비 좋음)
    a, b = 1, 1
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        for i in range(1, n):
            a, b = b, a + b
    return a

for i in range(a):                              # 입력 수만큼 반복
    iterate = int(input())                      # 피보나치 수열 n번째 수
    if iterate == 0:                            # 만약 0번째 수면
        print(1, 0)                             # 1, 0 출력
    else:                                       # 아니면
        print(fib(iterate-1), fib(iterate))     # 피보나치 수열 n-1, n번째 수 출력