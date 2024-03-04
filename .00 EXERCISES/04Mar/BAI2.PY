import sys
sys.stdin = open("BAI2.INP", "r")
sys.stdout = open("BAI2.OUT", "w")

ax,ay,cx,cy = map(int, input().split())
rong = abs(ax - cx)
dai = abs(ay - cy)
dt = rong*dai
cv = (rong+dai)*2

if dt:
    print(cv,dt)
else:
    print(-1)


