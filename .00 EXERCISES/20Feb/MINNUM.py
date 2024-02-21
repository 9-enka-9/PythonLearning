import sys
# sys.stdin = open("MINNUM.INP",'r')
# sys.stdout = open("MINNUM.OUT", 'w')

n, s = map(int, input().split())

if (9*n) < s:
    print(-1)
else:
    a = [9 for i in range(n)]
    for i in range(n):
        while ((a[i]>1 and i==0) or (a[i]>0 and i>0)) and sum(a) > s:
            a[i]-=1
        if sum(a) == s:
            break
    
    for i in range(n):
        print(a[i], end ="")