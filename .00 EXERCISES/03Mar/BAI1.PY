import sys
sys.stdin = open("BAI1.INP","r")

n = int(input())
ssh1 = 0
ssh2 = 0
tsh1 = 0
tsh2 = 0
s = 0
if n%2==0:
    ssh2 = ((-n)-(-2))/(-2) + 1
    tsh2 = (((-n)+(-2))*ssh2)/2
    n-=1
    ssh1 = (n-1)/2+1
    tsh1 = ((n+1)*ssh1)/2
else:
    ssh1 = (n-1)/2 + 1
    tsh1 = ((n+1)*ssh1)/2
    n-=1
    ssh2 = ((-n)-(-2))/(-2) + 1
    tsh2 = (((-n)+(-2))*ssh2)/2

s = tsh1 + tsh2
with open("BAI1.OUT","w") as f:
    out = f"{int(s)}"
    f.write(out)
