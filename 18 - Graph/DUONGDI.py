import sys, copy
sys.stdin = open("DUONGDI.inp", 'r')

n, m, start, end = map(int, input().split())
a = [[0 for i in range(n+1)] for i in range(n+1)]
check = [0 for i in range(n+1)]
for i in range(m):
    x, y, z = map(int, input().split())
    a[x][y] = z
    a[y][x] = z
index = 1

pathmax = []
path = []
smax = 0
def dfs(u):
    global pathmax, smax
    path.append(u)
    check[u] = index
    if u == end:
        s = 0
        for i in range(len(path)-1):
            s += a[path[i]][path[i+1]]
        if not pathmax or s < smax:
            pathmax = copy.deepcopy(path)
            smax = s
    else:
        for v in range(n+1):
            if check[v] == 0 and a[u][v] != 0:
                dfs(v)
    path.pop()
    check[u]=0

dfs(start)
print(pathmax)
