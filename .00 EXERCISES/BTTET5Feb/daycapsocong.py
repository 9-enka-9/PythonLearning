n = int(input())
arr = list(map(int, input().split()))

lenSubArr = [2] * n
maxLenSubArr = 2

for i in range(n-2):
    add = arr[i+1] - arr[i]
    j=i+1
    while arr[j+1] - arr[j] == add:
        lenSubArr[i]+=1
        if j==n-2:
            break
        j+=1
    if lenSubArr[i] > maxLenSubArr:
        maxLenSubArr = lenSubArr[i]

for i in range(n):
    if maxLenSubArr == lenSubArr[i]:
        for j in range(i, i+maxLenSubArr):
            print(arr[j],end=' ')
        break