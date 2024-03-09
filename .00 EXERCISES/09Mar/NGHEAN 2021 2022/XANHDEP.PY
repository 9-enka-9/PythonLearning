import sys
sys.stdin = open("XANHDEP.INP", "r")
sys.stdout = open("XANHDEP.OUT", "w")

n = int(input())
s = []
for i in range(n):
    s.append(input())

m=0
for i in range(n):
    count = 1
    f = s[i][0]
    for j in range(1, len(s[i])):
        if f == s[i][j]:
            count +=1
        else:
            m = max(m,count)
            count = 1
            f = s[i][j]

print(m)
    

