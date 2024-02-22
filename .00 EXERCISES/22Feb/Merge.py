import sys

# sys.stdin = open('MERGE.INP','r')
# sys.stdout = open('MERGE.OUT','w')

x, y, k = map(int, input().split())
z = []

def boi(num, n):
    res = [num]
    for i in range(2,n+1):
        res.append(i*num)
    return res

def addItem(li):
    for item in li:
        if item not in z:
            z.append(item)

if x == y:
    z = boi(x, k-1)
    print(z[k-1])
else:
    xx = boi(x, k-1)
    yy = boi(y, k-1)
    addItem(xx)
    addItem(yy)
    z.sort()
    print(z[k-1])