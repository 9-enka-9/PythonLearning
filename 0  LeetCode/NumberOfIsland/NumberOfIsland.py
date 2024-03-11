def dfs(pos):
    global count, mark
    change = ((0,1), (1,0), (-1,0), (0,-1))
    for x,y in change:
        if (x+pos[0]>=0) and (y+pos[1]>=0)\
           and x+pos[0]<n and y+pos[1]<m\
           and (mark[x+pos[0]][y+pos[1]]==False)\
           and (a[x+pos[0]][y+pos[1]]!='0'):
            mark[x+pos[0]][y+pos[1]] = True
            dfs([x+pos[0],y+pos[1]])

import sys
sys.stdin = open("NumberOfIsland.INP", "r")

a=[]
while True:
    
    try:
        line = input()
        if line:
            a.append(line.split())
        else:
            break
    except EOFError:
        break
n = len(a)
m = len(a[0])
count = 0
mark = [[False]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if not mark[i][j] and a[i][j] == '1':
            dfs([i,j])
            count+=1

print(count)
