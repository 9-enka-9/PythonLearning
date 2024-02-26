import sys
sys.stdin = open("ViTriCuoiCungCuaMotPhanTuNhoHonX.INP", "r")

n, x = map(int, input().split())
a = list(map(int, input().split()))

def bs(n, a, x):
    l, r = 0, n-1
    res = -1
    while l<=r:
        m = (l+r)//2
        if a[m] <= x:
            res = m
            l = m+1
        else:
            r = m-1
    return res

ex = bs(n, a, x)
print(ex)
