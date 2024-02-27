import sys
sys.stdin = open("MULTIPLE.INP","r")

n, q = map(int, input().split())

s = 1
turn = 1
for i in range(1,n):
    turn *= q
    s += turn

print(s)
