import sys, math
sys.stdin = open("UCLN.INP","r")
with open("UCLN.OUT","w") as f:
    n = int(input())
    a = list(map(int, input().split()))
    m = 1
    for i in range(n-1):
        ucln = math.gcd(a[i],a[i+1])
        m = max(ucln, m)
    output = str(m)
    f.write(output)
