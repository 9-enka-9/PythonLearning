import sys
from math import gcd, sqrt
sys.stdin = open("BAI4.INP","r")

def uoc(num):
    u = [1]
    for i in range(2,int(sqrt(num))+1):
        if num%i == 0:
            u.append(i)
            if i!=num:
                u.append(num//i)
    if num!=1:
        u.append(num)
    return u

t = int(input())
n=[]
a=[]
m = []
for i in range(t):
    n.append(int(input()))
    a.append(list(map(int, input().split())))
    m.append(min(a[i]))

for i in range(t):
    uc = uoc(m[i])
    for j in range(n[i]):
        for k in range(len(uc)):
            if a[i][j]%uc[k]!=0:
                uc.pop(k)
    print(len(uc))

