import sys
sys.stdin = open("BOBASO.INP", "r")
sys.stdout = open("BOBASO.OUT", "w")

n = int(input())
a = list(map(int, input().split()))

m = 2*a[1]+abs(a[2]-a[0])
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            t=2*a[j]+abs(a[k]-a[i])
            if m<t:
                m =t

print(m)
