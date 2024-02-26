import sys
sys.stdin = open("ViTriDauTienCuaMotPhanTuLonHonX.INP", "r")
with open("ViTriDauTienCuaMotPhanTuLonHonX.OUT", "w") as f:
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    def binarySearch(a, n, x):
        res = -1
        l = 0
        r = n-1
        while l <= r:
            m = (l+r)//2
            if a[m] > x:
                res = m
                r = m - 1
            elif a[m] <= x:
                l = m + 1
        return res
    out = str(binarySearch(arr, n, x)+1)
    f.write(out)
