import sys
sys.stdin = open("TERACING.INP", "r")

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
dic = {a[0]:1}
ans = 0

for i in range(1, n):
    if a[i]>k and dic.get(a[i]-k)!=None:
        ans += dic[a[i]-k]
    if dic.get(a[i]) == None:
        dic[a[i]] = 1
    else:
        dic[a[i]] +=1

print(ans)
