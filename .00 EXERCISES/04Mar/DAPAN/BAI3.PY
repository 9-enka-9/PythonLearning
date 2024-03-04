import sys
sys.stdin = open("BAI3.INP","r")
sys.stdout = open("BAI3.OUT", "w")

n = int(input())
a = list(map(int, input().split()))

p = [a[0]]
for i in range(1,n):
    p.append(p[i-1]+a[i])

mn = p[0]
s = p[0]
for i in range(1, n):
    s = max(p[i]-mn, s)
    mn = min(mn, p[i])

print(s)
