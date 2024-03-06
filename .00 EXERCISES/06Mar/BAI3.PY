def check(a, start, end, k):
    dic = {}
    for i in range(start, end):
        dic[a[i]] = 1
    return len(dic) == k

import sys
sys.stdin = open("BAI3.INP", "r")
sys.stdout = open("BAI3.OUT", "w")

n, k = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(k, n):
    for start in range(n-i+1):
        c += check(a, start, start+i, k)

print(c)

