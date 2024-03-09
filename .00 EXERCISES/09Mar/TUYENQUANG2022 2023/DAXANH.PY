import sys
sys.stdin = open("DAXANH.INP", "r")
sys.stdout = open("DAXANH.OUT", "w")

n, k = map(int, input().split())
a = [0] + list(map(int, input().split())) + [0]
s=[0, a[1]]
for i in range(1,n):
    s.append(s[i]+a[i+1])
##print(a)
##print(s)

t = 0
for i in range(1,n-2*k+1):
    t1 = s[i+k-1] - s[i-1]
    t2 = s[i+k+k-1] - s[i+k-1]
    if t<t1-t2:
        t=t1-t2
    elif t<t2-t1:
        t=t2-t1

print(t)
