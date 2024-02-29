import sys
sys.stdin = open("SieveLeftToRight.py", "r")

l, r = map(int, input().split())

prime = [True for i in range(r-l+3)]

def sang(l, r):
    global prime
    end = int(sqrt(r))
    for i in range(2, end):
        for j in range(max(i*i, ((l+i-1)//i)*i), i):
            prime[j-l] = False

for i in range(l,r):
    

