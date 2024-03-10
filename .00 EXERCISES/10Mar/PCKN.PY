def canJoin(c, b):
    if b == 0 or c==0: return True
    while c>0 and b>0:
        if (c%10)+(b%10)>=10:
            return False
        c/=10
        b/=10
    return True

##import sys
##sys.stdin = open("PCKN.INP", "r")

n = int(input())
a = list(map(int, input().split()))
joined = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i!=j and canJoin(a[i],a[j]):
            ok = True
            for k in joined[i]:
                if not canJoin(a[j], k):
                    ok = False
                    break
            if ok:
                joined[i].append(a[j])

c = 0
for i in range(n):
    t = 0
    for j in range(len(joined[i])):
        if a[i] in joined[j]:
            t+=1
    c = max(c,t+1)

print(c)
