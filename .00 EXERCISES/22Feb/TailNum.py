import sys

# sys.stdin = open('TAILNUM.INP','r')
# sys.stdout = open('TAILNUM.OUT','w')

n, m = map(int, input().split())
s = 1
for i in range(m):
    s*=n
    s%=1000
s = str(s)
s = '0'+s
for i in range (len(s)-2, len(s)):
    print(s[i], end="")

print(finally)
