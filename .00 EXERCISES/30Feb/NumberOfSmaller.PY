import sys
sys.stdin = open("NumberOfSmaller.INP", "r")

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i, j = 0, 0
while i<n and j<m:
    if a[i]<b[j]:
        i+=1
    else:
        print(i, end = " ")
        j+=1

while j < m:
    print(i, end = " ")
    j+=1


