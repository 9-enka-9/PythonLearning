##import sys
##sys.stdin = open("THCB.INP", "r")

n, k, b = map(int, input().split())
a = [1]*(n+1)
a[0]=0
for i in range(b):
    a[int(input())] = 0

s=[0]
for i in range(1, n+1):
    s.append(s[i-1]+a[i])

c=n
for i in range(1, n-k):
    c = min(k-(s[i+k-1]-s[i-1]), c)

print(c)

