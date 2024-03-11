import sys
sys.stdin = open("MULTIPLE.INP", "r")
sys.stdout = open("MULTIPLE.OUT", "w")

n, q = map(int, input().split())
s = 1
el = q
MOD = 2023
for i in range(1,n):
    s += (q)%MOD
    q*=el

print(s)
