import sys
sys.stdin = open("BAI1.INP","r")

n = int(input())

s = 0
if n>0 and n<=50:
    s += 2000*n
elif n>50 and n<=100:
    s += 50*2000 + (n-50)*3000
elif n>100:
    s += 50*2000 + 50*3000 + (n-100)*4000

print(s)
