import sys
from math import sqrt
sys.stdin = open("CHINHPHUONG.INP", "r")

def isCP(num):
    cnum = sqrt(num)
    if cnum == int(cnum):
        return True
    return False

with open("CHINHPHUONG.OUT", "w") as f:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s = 0
    c = 0
    for i in range(n):
        if isCP(a[i]):
            s += a[i]
            c +=1
        if c==2:
            break
    if c==2:
        out = f"{s}"
    else:
        out = "-1"
    f.write(out)
