def sieve(n):
    arr = [True for i in range(n+3)]
    arr[0]=arr[1]=False
    for i in range(2, int((n+3)**0.5)):
        if arr[i]:
            for j in range(i*i, n+3, i):
                arr[j] = False

    return [i for i in range(2,n+3) if arr[i]]

def f(N):
    

import sys

sys.stdin = open("BAI1.INP", "r")
##sys.stdout = open("BAI1.OUT", "w")

a = []
m = 0
while True:
    try:
        t = input()
        if not t:
            break
        a.append(int(t))
        m = max(a[-1],m)
    except EOFError:
        break

prime = sieve(m)
n = len(a)
print(prime)

for i in range(n):
    print(f(a[i]))



