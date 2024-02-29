import sys
sys.stdin = open("TONGUOC.INP", "r")

n = 6

def countDiv(num):
    s = 2
    for i in range(2,int(num**0.5)+1):
        if num % i==0:
            s+=1
            if num//i!=i:
                s+=1
    return s

def sumDiv(num):
    s = 1+num
    for i in range(2,int(num**0.5)+1):
        if num % i==0:
            s+=i
            if num//i!=i:
                s+=num//i
    return s
    
print(countDiv(n))
