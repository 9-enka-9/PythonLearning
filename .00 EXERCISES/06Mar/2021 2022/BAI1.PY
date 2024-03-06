import sys
sys.stdin = open("BAI1.INP", "r")
sys.stdout = open("BAI1.OUT", "w")

n = int(input())
a = []
dong = [0 for i in range(n)]
cot = [0 for i in range(n)]
for i in range(n):
    a.append(list(map(int, input().split())))
    dong[i] = sum(a[i])

for i in range(n):
    for j in range(n):
        cot[i] += a[j][i]

c=0
for i in range(n):
    for j in range(n):
        if dong[i] == cot[j]:
            c+=1

print(c)

