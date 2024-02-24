import sys
sys.stdin = open('DANGNHAP.INP','r')
sys.stdout = open('DANGNHAP.OUT','w')

n = int(input())
s = []
for i in range(n):
    s.append(input())

count = 0
ans = "login"
res = []
for i in range(n):
    index = 0
    for j in range(len(s[i])):
        if s[i][j] == ans[index]:
            print(s[i][j])
            index +=1
    if index >= len(ans):
        count += 1
        res.append(i)

print(count)
for i in res:
    print(i+1, end=' ')

