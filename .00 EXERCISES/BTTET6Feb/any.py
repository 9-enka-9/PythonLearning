n = int(input())
arr = list(map(int, input().split()))

def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a

def isPrime(num):
    if num>=2:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    return False

s=0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            gcdAll = gcd(arr[i], gcd(arr[j], arr[k]))
            if gcdAll>1 and not isPrime(gcdAll):
                s+=1

print(s)
