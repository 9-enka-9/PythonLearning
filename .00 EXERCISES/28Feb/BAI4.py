import sys
sys.stdin = open("BAI4.INP","r")
s = input().split()
s = ' '.join(s)
s = s.title()
out = f"{s}"

with open("BAI4.OUT","w") as f:
    f.write(out)
