import sys

sys.stdin = open("SUM.INP", "r")
sys.stdout = open("SUM.OUT", "w")

n = int(input())
a = [0] + list(map(int, input().split()))
s = [0]
for i in range(1,n+1):
    s.append(s[i-1] + a[i])

c=0
for i in range(n):
    for j in range(1, n-i+1): 
        if s[j+i] - s[j-1] == 0:
            c+=1

print(c)

