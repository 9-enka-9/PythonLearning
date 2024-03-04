import sys
sys.stdin = open("BAI4.INP", "r")
sys.stdout = open("BAI4.OUT", "w")

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a.sort()
res = a[0]-1
for i in range(n-1, 1,-1):
    if not a[i]-1 == a[i-1]:
        res = a[i]-1
        break

print(res)

