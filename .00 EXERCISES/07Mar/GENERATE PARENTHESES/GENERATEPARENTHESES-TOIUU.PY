import sys
sys.stdin = open("GENERATEPARENTHESES.INP", "r")

def generate(s, op, cl):
    global n
    if op > n/2 or cl > op: return
    if op == n/2 == cl: print(s)
    generate(s+"(", op + 1, cl)
    generate(s+")", op, cl+1)

n = int(input())
s = ""
n = n*2
generate(s, 0, 0)

