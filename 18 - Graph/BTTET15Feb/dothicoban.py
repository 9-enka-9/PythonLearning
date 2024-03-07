n, m = map(int, input().split())
a = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(m):
    x, y, z = map(int, input().split())
    a[x][y] = z
    a[y][x] = z

for i in range(1,n+1):
    print(sum(a[i]))