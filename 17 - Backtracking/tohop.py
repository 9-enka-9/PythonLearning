n, k = map(int, input().split())
x=[0]*k

def backtrack(i):
    if i == k:
        print(x)
        return
    for j in range(x[i-1]+1,n-k+i+2):
        if len(x)>=i+1:
            x.pop(i)
        x.insert(i,j)
        backtrack(i+1)

backtrack(0)