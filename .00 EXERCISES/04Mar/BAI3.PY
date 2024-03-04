import sys
sys.stdin = open("BAI3.INP", "r")
sys.stdout = open("BAI3.OUT", "w")

n = int(input())
a = list(map(int, input().split()))
s = -int(1e9)
for i in range(1, n):
    for j in range(n-i):
        t = sum(a[j:j+i])
        s = max(s,t)

print(s)
