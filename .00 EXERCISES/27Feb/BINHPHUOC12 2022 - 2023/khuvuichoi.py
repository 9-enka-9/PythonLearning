import sys
sys.stdin = open("khuvuichoi.inp", "r")

start, end = map(int, input().split())

s = 0
c = 0
for i in range(start+1, end+1):
    if i<=12 and c<4:
        s+=6
    elif i>12 and c<4:
        s+=10
    elif i<=12 and c>=4:
        s+=3
    else:
        s+=5
    c+=1

print(s)
