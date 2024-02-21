n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
res=[]

for i in range(n):
    shang = sum(arr[i]) - arr[i][i]
    scot = 1
    for j in range(n):
        if arr[j]!=arr[i]:
            scot*=arr[j][i]
    if arr[i][i]>scot and arr[i][i]<shang:
        res.append([i,i,arr[i][i]])

if res:
    print('YES')
    for i in range(len(res)):
        print(res[i][0]+1, res[i][1]+1, res[i][2])
else:
    print('NO')
