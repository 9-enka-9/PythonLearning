import sys
sys.stdin = open("SUB.INP", "r")

n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
s = [0]
res = n+1

def bs(k, d, c, i):
    p = -1
    while d <= c:
        g = (d+c)//2
        if s[i] - s[g] >= k:
            p = g
            d = g+1
        else:
            c = g-1
    return p


for i in range(1,n+1):
    s.append(s[i-1]+a[i])

for i in range(1, n+1):
    p = bs(k, 0, i, i)
    if p >= 0:
        res = min(res, i-p)

print(res)
