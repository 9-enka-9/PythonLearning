import sys
sys.stdin = open("Sort.inp","r")

a = list(map(int, input().split()))
n = len(a)
for i in range(n-1):
    for j in range(i+1, n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
