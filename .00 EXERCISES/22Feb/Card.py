import sys

# sys.stdin = open('CARD.INP','r')
# sys.stdout = open('CARD.OUT','w')

n = int(input())
a = list(map(int, input().split()))
check = {}

for i in a:
    if i not in check:
        check[i]=1
    else:
        check[i]+=1

res = []
for key in check:
    if check[key]<2:
        res.append(key)

res.sort()
for i in res:
    print(i, end=" ")