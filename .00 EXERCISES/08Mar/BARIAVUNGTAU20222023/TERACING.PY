import sys
sys.stdin = open("TERACING.INP", "r")
sys.stdout = open("TERACING.OUT", "w")

n, k = map(int, input().split())
a = list(map(int, input().split()))
dic = {}
for i in range(n):
    if dic.get(a[i]) == None:
        dic[a[i]]=1
    else:
        dic[a[i]]+=1

s=0
for i in dic.keys():
    if dic.get(i+k):
        s += (dic[i]*dic[i+k])

print(s)
