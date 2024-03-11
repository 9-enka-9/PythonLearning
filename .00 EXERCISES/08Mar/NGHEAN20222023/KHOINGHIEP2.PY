class cty:
    def __init__(self, a, b):
        self.a = a
        self.b = b

import sys, queue
sys.stdin = open("KHOINGHIEP.INP", "r")
sys.stdout = open("KHOINGHIEP.OUT", "w")

n = int(input())
x = []
for i in range(n):
    u,v = map(int, input().split())
    x.append(cty(u,v))
x.sort(key = lambda t: t.a)
x = [cty(0,0)] + x
pQ = queue.PriorityQueue()
k = 0
ans = 0
for i in range(n, 0, -1):
    pQ.put(x[i].b)
    while x[i].a > i-1+k:
        ans += pQ.get()
        k += 1

print(ans)
