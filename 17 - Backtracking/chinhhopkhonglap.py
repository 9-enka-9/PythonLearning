n, k = map(int, input().split())
x=[]
isUsed=[False]*(n+2)

def backtrack(i):
    if i == k:
        print(x)
        return
    for j in range(1,n+1):
        if not isUsed[j]:
            if len(x)>=i+1:
                x.pop(i)
            x.insert(i,j)
            isUsed[j] = True
            backtrack(i+1)
            isUsed[j] = False

backtrack(0)