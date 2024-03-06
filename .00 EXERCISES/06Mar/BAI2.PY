import sys
sys.stdin = open("BAI2.INP", "r")
sys.stdout = open("BAI2.OUT", "w")

n = int(input())
a = list(map(int, input().split()))
c=0
for i in range(n-1):
    for j in range(i+1, n):
        c+=(a[i] == -a[j])

print(c)
