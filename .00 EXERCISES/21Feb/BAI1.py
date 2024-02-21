import sys
# sys.stdin = open('BAI1.INP', 'r')
# sys.stdout = open('BAI2.OUT', 'w')

n = int(input())
arr = [[0 for j in range(n+2)] for i in range (n+2)]
b = [[0 for j in range(n+2)] for i in range(n+2)]

for i in range(1, n+1):
    arr[i] = list(map(int, input().split()))
    arr[i].insert(0,0)
    arr[i].insert(n+2,0)

for i in range(1, n+1):
    for j in range(1, n+1):
        b[i][j] = arr[i][j] + arr[i+1][j] + arr[i-1][j] + arr[i][j+1] + arr[i][j-1]

for i in range(1,n+1):
    for j in range(1,n+1):
        print(b[i][j], end=" ")
    print()
