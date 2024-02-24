import sys
sys.stdin = open("TICHLN.inp", "r")

with open('TICHLN.out', 'w') as f:
    a, b, c = map(int, input().split())
    m = a*b
    if b*c>m:
        m = b*c
    if a*c>m:
        m = a*c
    output = str(m)
    f.write(output)
