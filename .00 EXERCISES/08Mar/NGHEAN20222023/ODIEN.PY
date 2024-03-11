import sys
sys.stdin = open("ODIEN.INP", "r")
sys.stdout = open("ODIEN.OUT", "w")

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = 1
a.sort()
c = 0
for i in range(n-1,0,-1):
    s += (a[i]-1)
    c += 1
    if s>=m:
        break
if s<m:
    print(-1)
else:
    print(c)
