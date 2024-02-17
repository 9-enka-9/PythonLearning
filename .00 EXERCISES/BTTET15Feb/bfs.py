n, m, start = map(int, input().split())

a = []
for i in range(n+1):
    t = []
    for j in range(n+1):
        t.append(0)
    a.append(t)
    
check = []
for i in range(n+1):
    check.append(False)

for i in range(m):
    x, y = map(int, input().split())
    a[x][y]=1
    a[y][x]=1
    
path = []

def dfsTitDuong(u):
    flag = True
    check[u]=True
    for v in range(1,n+1):
        if not check[v] and a[u][v]:
            dfs(v)
            flag = False
    if flag:
        print(u, end = " ")
        
def dfs(u):
    path.append(u)
    check[u]=True
    for v in range(1,n+1):
        if not check[v] and a[u][v]:
            dfs(v)

def bfs(start):
    queue = [start]
    while queue:
        u = queue[0]
        queue.pop(0)
        if not check[u]:
            print(u, end= " ")
            check[u]=1
            for v in range(1, n+1):
                if check[v] == False and a[u][v] == 1:
                    queue.append(v) 

dfs(start)
print(path)
