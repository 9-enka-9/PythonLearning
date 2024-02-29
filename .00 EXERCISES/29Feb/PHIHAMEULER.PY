import sys
sys.stdin = open("PHIHAMEULER.INP","r")

num = int(input())

def phi(num):
    res = num
    for i in range(2, int(num**0.5)):
        if num%i==0:
            while num%i == 0:
                num//=i
            res -= res/i
    if num!=1:
        res-=res/num
    return res
    
print(phi(num))
