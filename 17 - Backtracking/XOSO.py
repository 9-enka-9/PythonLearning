'''
n=4, k=2
6 7 6 5
backtrack(0): a[0]=6 mark[0]
    backtrack(0) => skip
    backtrack(1): a[1] = 7
    => 6 7 => max:7
    backtrack(2): a[2] = 6
    => 6 6 => max: 6
    backtrack(3): a[3] = 5
    => 6 5 => max: 6
backtrack(1): a[1] = 7 mark[1]
    backtrack(0): => skip
    backtrack(2): a[2] = 6
    => 7 6 => max: 7
    backtrack(3): a[3] = 5
    => 7 5 => max: 7
backtrack(2): a[2] = 6 mark[2]
    backtrack(0) => skip
    backtrack(1) => skip
    backtrack(2) => skip
    backtrack(3): a[3] = 5
    => 6 5 => max: 6
'''
def backtrack(i):
    global n,s,mark,x
##    print(x)
    for v in range(n):
        if not mark[v]:
            x[i]=a[v]
            if k-1 <= i:
                print(x)
                s+=max(x)
            else:
                mark[v] = True
                backtrack(i+1)
                mark[v] = False
    print()


import sys
sys.stdin = open("XOSO.inp" ,"r")

n, k = map(int, input().split())
a = list(map(int, input().split()))
x = [0]*(k)
mark = [False]*n
s = 0
for i in range(n):
    if not mark[i]:
        x[0] = a[i]
        mark[i] = True
        backtrack(1)

print(s)
