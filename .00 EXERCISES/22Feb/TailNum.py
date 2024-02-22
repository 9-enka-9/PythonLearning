import sys

# sys.stdin = open('TAILNUM.INP','r')
# sys.stdout = open('TAILNUM.OUT','w')

n, m = map(int, input().split())
s = str(n**m)
s = '0'+s
for i in range (len(s)-2, len(s)):
    print(s[i], end="")