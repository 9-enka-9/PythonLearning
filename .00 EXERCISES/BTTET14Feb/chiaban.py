n = int(input())
a = list(map(int, input().split()))

a.sort()
def divide(n, a):
    ban = [0]*(n+1)
    numFinding = [4]*(n+1)
    bIndex = 0
    ban[bIndex] += a[0]
    a.pop(0)
    numFinding[bIndex] = 4 - ban[bIndex]
    if numFinding[bIndex] == 0:
        bIndex += 1
    while a and bIndex<n:
        isSolved = False
        for i in range(len(a)):
            if a[i] == numFinding[bIndex]:
                ban[bIndex] += a[i]
                numFinding[bIndex] = 4 - ban[bIndex]
                a.pop(i)
                if numFinding[bIndex] == 0:
                    bIndex += 1
                isSolved = True
                break
        if not isSolved and numFinding[bIndex]>1:
            numFinding[bIndex] -= 1
        elif not isSolved and numFinding[bIndex]<=1:
            bIndex += 1
            
    # for i in range(len(a)):
    #     if ban[bIndex] + a[i] <= 4:
    #         ban[bIndex] += a[i]
    #         numFinding[bIndex] -= a[i]
    #     else:
    #         bIndex += 1
    #         ban[bIndex] += a[i]
    return ban

ban = divide(n, a)
count=0
for i in range(len(ban)):
    if ban[i]!=0:
        count+=1
    else:
        break

print(count)
