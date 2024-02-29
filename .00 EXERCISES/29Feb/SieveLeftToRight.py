import sys
sys.stdin = open("SieveLeftToRight.INP", "r")

l, r = map(int, input().split())

prime = [True for i in range(r-l+3)]

def sang(l, r):
    global prime
    end = int(r**0.5)+1
    print(end)
    print(r+1)
    for i in range(2, end):
        for j in range(max(i*i, (l+i-1)//i*i), r+1, i):
            prime[j-l] = False
            
sang(l,r)
for i in range(max(l,2),r):
    if prime[i-l]:
        print(i)
