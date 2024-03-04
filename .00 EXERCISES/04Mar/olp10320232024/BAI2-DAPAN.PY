import sys
sys.stdin = open("BAI2.INP","r")
sys.stdout = open("BAI2.OUT", "w")

ax,ay,cx,cy = map(int, input().split())

if (ax == ay and ay == cx and cx == cy) or (ax == cx) or (ay == cy):
    print(-1)
else:
    rong = abs(ax-cx)
    dai = abs(ay-cy)
    cv = 2*(rong+dai)
    dt = rong*dai
    print(cv,dt)
