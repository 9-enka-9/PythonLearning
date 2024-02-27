import sys
from math import sqrt
sys.stdin = open("PAIRPBRO.INP", "r")

n, k = map(int, input().split())
nto = [True for i in range(n+1)]

def sang(num):
    des = int(sqrt(num))
    nto[0] = False
    nto[1] = False
    for i in range(2,des):
        if nto[i]:
            for j in range(i*i, num+1, i):
                nto[j] = False

sang(n)
count = 0
for i in range(n+1-k):
    if nto[i] and nto[i+k]:
        count +=1

print(count)
