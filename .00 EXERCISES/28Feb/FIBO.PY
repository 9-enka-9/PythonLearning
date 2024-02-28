import sys
sys.stdin = open("FIBO.INP","r")

n = int(input())
a = []
out =""
c = 1
dic = {1:1,}
def fibo(n):
    global a, c
    a.append(1)
    a.append(1)
    for i in range(2,n):
        t= a[i-1]+a[i-2]
        if t>100:
            t = t%100
        a.append(t)
        dic[t]=1

fibo(n)
out += f'''{a[n-1]}
{len(dic)}'''
print(a)
with open("FIBO.OUT", "w") as f:
    f.write(out)
