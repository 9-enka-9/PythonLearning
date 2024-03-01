import sys
sys.stdin = open("NumberOfEqual.inp", "r")

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i, j = 0, 0
res = 0
while i<n and j<m:
    if a[i]<b[j]:
        i+=1
    elif a[i]>b[j]:
        j+=1
    else:
        t = a[i]
        c1, c2 = 0, 0
        while i<n and a[i]==t:
            c1+=1
            i+=1
        while j<m and t == b[j]:
            c2+=1
            j+=1
        res += (c1*c2)
            
print(res)
