import sys
sys.stdin = open("SegmentWithSmallSum.inp", "r")

n, s = map(int,input().split())
a = list(map(int, input().split()))
su = 0
l = 0
res = 0
for r in range(n):
    su += a[r]
    while su>s:
        su -= a[l]
        l+=1
    res = max(res, r-l+1)

print(res)
