import sys
sys.stdin = open("Daycondondieudainhat.inp", "r")
##sys.stdout = open("Daycondondieudainhat.out", "w")

n = int(input())
a = list(map(int, input().split()))
L = [1]*n
for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            L[i] = max(L[i], L[j]+1)

print(max(L))

