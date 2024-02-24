import sys
sys.stdin = open('ThanhPhanLienThong.INP', 'r')

n, m, start = map(int, input().split())
a = [[0 for i in range(n+1)] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    a[x][y] = 1
    a[y][x] = 1
check = [0 for i in range(n+1)]
index = 1
path = []
def dfs(u):
    path.append(u)
    check[u]=index
    for v in range(1, n+1):
        if check[v]==0 and a[u][v]:
            dfs(v)


while index < n+1:
    if check[index]==0:
        dfs(index)
        print(path)
        path.clear()
    index += 1
