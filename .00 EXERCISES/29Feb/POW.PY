import sys
sys.stdin = open("POW.INP","r")

MOD = int(1e9)

def pow1(a, b):
    res = 1
    while b:
        if b%2==1:
            res *= a
        b/=2
        a*=a
        a%=MOD
        res%=MOD
    return res

a, b = map(int, input().split())
print(pow1(a,b))
