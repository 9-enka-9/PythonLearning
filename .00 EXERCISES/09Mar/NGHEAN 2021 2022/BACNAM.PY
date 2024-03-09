import sys
sys.stdin = open("BACNAM.INP", "r")
##sys.stdout = open("BACNAM.OUT", "w")

n = int(input())
a = list(map(int, input().split()))
start = a.index(1)
a = a[start:]+a[:start:1]
print(a)
chan = []
le = [1]
tr1=1
tr2=0
vong=0
i=0
a.pop(0)
bre = 0
while a!=[] and bre<100:
    print(a[i])
    if tr2+2 == a[i]:
        chan.append(a.pop(i))
        tr2 = chan[-1]
    elif tr1+2 == a[i]:
        le.append(a.pop(i))
        tr1 = le[-1]
    
    if a and a[i]==a[-1]:
        vong+=1
        i=0
    else:
        i+=1
    bre+=1
        
print(vong)
