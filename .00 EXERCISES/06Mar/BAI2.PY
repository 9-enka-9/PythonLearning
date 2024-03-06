def bs(a, n, x):
    l, r = 0, n-1
    while l<=r:
        m = (l+r)//2
        if a[m] == x:
            return 1
        elif a[m]<x:
            l = m+1
        elif a[m]>x:
            r = m-1
    return 0


import sys
sys.stdin = open("BAI2.INP", "r")
sys.stdout = open("BAI2.OUT", "w")

n = int(input())
a = list(map(int, input().split()))
a.sort()
c=0
for i in range(n-1):
    c += bs(a[i+1:n], n-i, -a[i])

print(c)
