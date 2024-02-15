n, k = map(int, input().split())

a = [n,n*2]
sumb4 = n
for i in range(2,k+1):
    a.append(0)
    a[i] = (a[i-1]*2 + sumb4) % (10**9+7)
    sumb4 += a[i-1]

print(a[k])