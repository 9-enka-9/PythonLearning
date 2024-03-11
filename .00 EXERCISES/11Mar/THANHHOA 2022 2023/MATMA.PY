import sys
sys.stdin = open("MATMA.INP", "r")
sys.stdout = open("MATMA.OUT", "w")

s = input()
dic = {}
for i in s:
    if dic.get(i)!=None:
        dic[i]+=1
    else:
        dic[i] = 1

su = 0
si = ""
for i in range(9, -1, -1):
    t= str(i)
    if dic.get(t) != None:
        su += i*dic[t]
        for j in range(0,dic[t]):
            si+=t

if si[-1]=='0' and su%3==0:
    print(si)
else:
    print(-1)



