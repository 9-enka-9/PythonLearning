import sys
sys.stdin = open("BAI3.INP", "r")

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
count=0
for i in range(n):
    if a[i]<=k:
        k-=a[i]
        count+=1
    if k-a[i+1]<0:
        break
    else:
        i += 1

print(count)
