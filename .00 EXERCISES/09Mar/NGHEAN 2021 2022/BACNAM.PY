import sys
sys.stdin = open("BACNAM.INP", "r")
sys.stdout = open("BACNAM.OUT", "w")

n = int(input())
a = list(map(int, input().split()))
start = a.index(1)
a = a[start:]+a[:start:1]
end=n
n-=2
chan, le = [], [1]
tr1, tr2 = 1, 0
vong=0
i=0
a.pop(0)
vongchan, vongle = 0, 0
while a!=[]:
    if tr2+2 == a[i]:
        chan.append(a.pop(i))
        tr2 = chan[-1]
        n-=1
        i-=1
    elif tr1+2 == a[i]:
        le.append(a.pop(i))
        tr1 = le[-1]
        n-=1
        i-=1
    
    if i>=n:
        vong+=1
        i=0
        if chan[-1] == n:
            vongchan = vong
        elif le[-1] == n-1:
            vongle = vong
    else:
        i+=1

print(vong)
