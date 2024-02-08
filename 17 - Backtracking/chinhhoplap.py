n, k = map(int, input().split())
x=[]

def backtrack(i):
    if i == k:
        print(x)
        return
    for j in range(1,n+1):
        if len(x)>i:
            x.pop(i)
        x.insert(i,j)
        backtrack(i+1)

backtrack(0)