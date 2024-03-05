import sys
sys.stdin = open("QUA.INP", "r")
##sys.stdout = open("QUA.OUT", "w")

n = int(input())
a = []
w = []
for i in range(n):
    ai,wi = map(int, input().split())
    a.append(ai)
    w.append(wi)

print(a,w)
