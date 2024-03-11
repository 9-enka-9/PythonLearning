import sys
sys.stdin = open("ROBOT.INP", "r")
sys.stdout = open("ROBOT.OUT", "w")

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

print(max(abs(x2-x1), abs(y2-y1)))

