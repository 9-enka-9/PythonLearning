def tusort(a, k):
    for i in range(n-1):
        for j in range(i,n):
            if a[i][k]<a[j][k]:
                a[i], a[j] = a[j], a[i]

import sys
sys.stdin = open("KHOINGHIEP.INP", "r")
##sys.stdout = open("KHOINGHIEP.OUT", "w")

n = int(input())
arr = []
e = 0
can = []
phi = 0
for i in range(n):
    a,b = map(int, input().split())
    arr.append([a,b])
    if a==0:
        can.append(i)

for i in can:
    e+=1
    arr.pop(i)
    n-=1

while n>0:
    
