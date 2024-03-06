import math

def sieve(n):
    global prime
    prime[0] = prime[1] = False
    for i in range(2, int(math.sqrt(n))):
        if prime[i]:
            for j in range(i*i, n, i):
                prime[j]=False


n,m = map(int, input().split())
a = list(map(int, input().split()))
q = []
prime = [True for i in range(int(1e4))]
sieve(int(1e4))
for i in range(m):
    u,v = map(int, input().split())
    q.append([u,v])

s = [a[0]]
for i in range(1, n):
    s.append(s[i-1]+a[i])

for i in range(m):
    x = s[q[i][1]-1] - s[q[i][0]-2]
    if x>0 and prime[s[q[i][1]-1] - s[q[i][0]-2]]:
        print(1)
    else:
        print(0)

