##import sys
##sys.stdin = open("DAYCONTANGDAINHAT.INP", "r")
##sys.stdout = open("DAYCONTANGDAINHAT.OUT", "w")

n = int(input())
a = [int(-1e9-1)]+list(map(int, input().split()))+[int(1e9+1)]
n+=2
f = [0 for i in range(n)]
f[0] = 1
for i in range(1,n):
    for j in range(1,i):
        if a[i]>a[j] and f[i]<f[j]+1:
            f[i] = f[j]+1

size = f[-1]
print(size)
##revet = []
##i = -1
##while True:
##    revet.append(a[i])
##    i = vet[i]
##    if i == 0:
##        break
##
##for i in range(size-2, 0, -1):
##    print(revet[i], end=" ")
