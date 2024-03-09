def sieve(n):
    global prime
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5)):
        if prime[i]:
            for j in range(i*i, n, i):
                prime[j]=False


import sys
sys.stdin = open("PAIRPBRO.INP", "r")
sys.stdout = open("PAIRPBRO.OUT", "w")

n, k = map(int, input().split())
prime = [True]*(n+2)
sieve(n+2)
c=0
for i in range(2,n-k):
    if prime[i] and prime[i+k]:
        c+=1

print(c)
