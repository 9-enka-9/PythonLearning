
import math

def sieve(n):
    global prime
    prime[0] = prime[1] = False
    for i in range(2, int(math.sqrt(n))):
        if prime[i]:
            for j in range(i*i, n, i):
                prime[j] = False
    

##def isPrime(num):
##    if num<=1: return False
##    for i in range(2, int(math.sqrt(num))+1):
##        if num%i==0:
##            return False
##    return True

def check(num):
    t = num
    s = 0
    rev = 0
    while t>0:
        s+=t%10
        rev = rev*10 + t%10
        t//=10
    if prime[s] and rev == num:
        return 1
    return 0

import sys
sys.stdin = open("BAI4.INP", "r")
sys.stdout = open("BAI4.OUT", "w")

l, r = map(int, input().split())
prime = [True for i in range(120)]
sieve(120)

c = 0
for i in range(l,r):
    c += check(i)

print(c)
