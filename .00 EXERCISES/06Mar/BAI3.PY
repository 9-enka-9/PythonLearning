def check(a,end, k):
    dic = {}
    for i in range(end):
        dic[a[i]] = 1
        if len(dic)>k:
            return 0
    if len(dic)==k:
        return 1
    return 0

import sys
sys.stdin = open("BAI3.INP", "r")
sys.stdout = open("BAI3.OUT", "w")

n, k = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(k, n):
    for start in range(n-i+1):
        c += check(a[start:start+i], i, k)

print(c)

