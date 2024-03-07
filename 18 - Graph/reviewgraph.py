import sys
sys.stdin = open('reviewgraph.inp','r')
##sys.stdout = open('reviewgraph.out', 'w')

n, m, start = map(int, input().split())
arr = [[0 for i in range(n+1)] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1
isUsed = [False]*(n+1)

road = []

def dfs(u):
    flag = False # kiểm tra cụt đường chưa
    isUsed[u] = True # kiểm tra đã thăm chưa
    road.append(u)
    for v in range(n+1):
        if not isUsed[v] and arr[u][v]:
            dfs(v)
            flag = True
            
    if flag == False:
        print(road)
    road.pop()
    isUsed[u] = False
        
dfs(start)
