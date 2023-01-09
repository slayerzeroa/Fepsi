import sys                          # sys로 input 받기
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x ,y):                      # dfs
    if x<=-1 or x>=n or y<=-1 or y>=m:  # case split
        return False

    if graph[x][y] == 1:            # case split
        graph[x][y] = 0             # graph reset
        dfs(x-1, y)                 # recursive(재귀)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True                 # print(1)

N = int(input())                    # iteration_number

for _ in range(N):                  # iterate
    m, n, k = map(int, input().split()) # status
    graph = []                          # create graph list
    for i in range(n):                  # iteration
        graph.append([0]*m)             # empty graph

    for _ in range(k):                  # generation 1
        y, x = map(int, input().split())
        graph[x][y] = 1

    result = 0                          # result = 0
    for i in range(n):                  # dfs process
        for j in range(m):
            if dfs(i, j):
                result += 1
    print(result)                       # print result