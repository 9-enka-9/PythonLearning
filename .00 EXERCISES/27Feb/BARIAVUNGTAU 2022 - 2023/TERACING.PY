import sys
sys.stdin = open("TERACING.INP", "r")
n, k = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(n):
    t = a.count(a[i]+k)
    if a.count(a[i]+k) > 0:
        c+=t
out = str(c)
print(out)
