import sys
sys.stdin = open("BAI3.INP", "r")
sys.stdout = open("BAI3.OUT", "w")

n = int(input())
a = list(map(int, input().split()))
s = None
for i in range(1, n):
    for j in range(n-i):
        t = sum(a[j:j+i])
        if s == None or s<t:
            s = t

print(s)
