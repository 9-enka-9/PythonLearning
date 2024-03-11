def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

import sys
sys.stdin = open("BAI1.INP", "r")

prime = []
for i in range(2, 1003):
    if isPrime(i):
        prime.append(i)

dp=[-10000]*(1003)
dp[0]=0
for x in prime:
    for s in range(1001, x-1, -1):
        for k in range(1,3):
            if s>= k*x:
                dp[s] = max(dp[s], dp[s - x*k] + k)

while True:
    try:
        line = input()
        if not line:
            break
        num = int(line)
        if num == 1:
            print(1)
        else:
            print(dp[num])
    except EOFError:
        break


