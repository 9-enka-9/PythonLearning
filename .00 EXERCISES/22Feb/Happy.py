import sys, math

sys.stdin = open("HAPPY.INP",'r')
sys.stdout = open("HAPPY.OUT",'w')

n = int(input())
a = list(map(int, input().split()))

def isPrime(num):
    if num>=2:
        for i in range(2, int(math.sqrt(num))+1):
            if num%i == 0:
                return False
        return True
    return False

count = 0 
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            res = math.gcd(math.gcd(a[i], a[j]), a[k]) 
            if not isPrime(res) and res>1:
                count += 1

print(count)
