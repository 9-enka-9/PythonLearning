import sys
sys.stdin = open("DAYCONTANGDAINHAT.INP", "r")
##sys.stdout = open("DAYCONTANGDAINHAT.OUT", "w")

a = [int(-1e7)]+list(map(int, input().split()))+[int(1e7)]
n = len(a)
f = [0 for i in range(n)]
f[0] = 1
f[1] = 2
vet = [0 for i in range(n)]

for i in range(2,n):
    for j in range(1,i):
        if a[i]>a[j] and f[i]<f[j]+1:
            f[i] = f[j]+1
            vet[i] = j

size = f[-1]
print(size-1)
revet = []
i = -1
while True:
    revet.append(a[i])
    i = vet[i]
    if i == 0:
        break

for i in range(size-2, 0, -1):
    print(revet[i], end=" ")
