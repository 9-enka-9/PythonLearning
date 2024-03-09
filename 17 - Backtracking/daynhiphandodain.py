def backtrack(k):
    global n
    for i in range(0,2):
        x[k]=i
        if k == n-1: print(x)
        else:
            backtrack(k+1)

n=3
x = [0]*(n)
backtrack(0)
