def dem(num,b):
    c=0
    for i in range(1,min(int(num**0.5)+1, int(b**0.5)+1)):
        if num%i==0 and b%(3*i)==0:
            c+=i
            t = num/i
            if t!=i and b%(3*t)==0:
                c+=num/i
    if b%(3*num)==0:
        c+=num
    return c

import sys
sys.stdin = open("TONGUOC.INP", "r")
sys.stdout = open("TONGUOC.OUT", "w")

a, b = map(int, input().split())
print(dem(a,b))
