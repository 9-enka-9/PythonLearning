import sys
sys.stdin = open("BAI2.INP" ,"r")
sys.stdout = open("BAI2.OUT", "w")

n, k, b = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

b = (b-1)%n
s=0
##while k>0:
##    s+=a[i]
##    if i>=n:
##        i=1
##    else:
##        i+=1
##    k-=1

for i in range(k):
    s+=a[(b+i)%n]

print(s)
