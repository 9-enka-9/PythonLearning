import math

def khh(num):
    s = 1
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            s+= i
            if num//i!=i:
                s+=(num//i)
    return s > num

import sys
sys.stdin = open("KHH.INP", "r")
sys.stdout = open("KHH.OUT", "w")

a, b = map(int, input().split())

c=0
##for i in range(a, b):
##    c += (prime[2] and prime[])    

for i in range(max(6,a),b+1):
    if khh(i):
        c+=1

print(c)

