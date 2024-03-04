def bs(arr, n, x):
    l,r = 0, n-1
    i=0
    while l<=r:
        i+=1
        m = (r+l)//2
        if arr[m] == x:
            return 1
        elif x>arr[m]:
            l = m+1
        elif x<arr[m]:
            r = m-1
    return 0

fi = [1,1]
end = 100
for i in range(2,end):
    fi.append(fi[i-1]+fi[i-2])

import sys
sys.stdin = open("BAI5.INP", "r")
sys.stdout = open("BAI5.OUT", "w")

n = int(input())
a = list(map(int, input().split()))

c = 0
for i in range(1, n+1):
    for j in range(n-i):
        s = sum(a[j:j+i])
        c += bs(fi,end,s)

print(c)
