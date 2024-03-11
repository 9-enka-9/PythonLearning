import sys, bisect
sys.stdin = open("DAYSODEP.INP", "r")
sys.stdout = open("DAYSODEP.OUT","w")

n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
chan = [0]*(n+3)
le = [0]*(n+3)

for i in range(1, n+1):
    chan[i] = chan[i-1]
    le[i] = le[i-1]
    if a[i]%2 == 0:
        chan[i]+=a[i]
    else:
        le[i]+=a[i]

ans = 0

def sub12():
    global ans
    for i in range(1,n):
        for j in range(i+1, n+1):
            x = chan[j] - chan[i-1]
            y = le[j] - le[i-1]
            if 0<x and 0<y and 0 <= x-y and x-y<= k:
                ans+=1

def sub34():
    global ans
    dic = {}
    q = [0,1]
    for r in range(2, n+1):
        l1 = bisect.bisect_left(chan, chan[r] - 1)
        l2 = bisect.bisect_left(le, le[r] - 1)
        l = min (l1,l2)
        while len(q)>0 and q[0]<=1:
            i = q[0]
            if dic.get(chan[i]-le[i] == None):
                dic[chan[i] - le[i]] = 1
            else:
                dic[chan[i] - le[i]] += 1
            q.pop(0)
        for t in range(k+1):
            if dic.get(chan[r] - le [r] - t) != None:
                ans += dic[chan[r] - le[r] - t]
        q.append(r)

if n<=2000: sub12()
else: sub34()

print(ans)

