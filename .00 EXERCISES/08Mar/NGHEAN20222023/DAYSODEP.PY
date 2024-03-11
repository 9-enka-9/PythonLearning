import sys
sys.stdin = open("DAYSODEP.INP","r")
sys.stdout = open("DAYSODEP.OUT", "w")

n, k = map(int, input().split())
a = [0] + list(map(int, input().split())) +[0]

c=[0 for i in range(n+2)]
l=[0 for i in range(n+2)]
for i in range(1,n+1):
    if a[i]%2 == 0:
        c[i]+=a[i]+c[i-1]
        l[i]+=l[i-1]
    else:
        l[i]+=a[i]+l[i-1]
        c[i]+=c[i-1]
##print(a)
##print(c)
##print(l)
count=0
for i in range(2,n+1):
    for j in range(1, n-i+2):
        chan = c[j+i-1] - c[j-1]
        le =   l[j+i-1] - l[j-1]
##        print(j, j+i-1, chan-le)
        if chan>0 and le>0 and (chan-le)<=k and (chan-le)>=0:            
            count+=1

print(count)
        
        
