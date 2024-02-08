n,t = map(int, input().split())
arr = list(map(int, input().split()))
        
lenOfMagic = 1
for size in range(n-1, 0, -1):
    for start in range(n-size):
        A = arr[start:start+size+1]
        maxA=max(A)
        minA=min(A)
        if maxA - minA <= t:
            lenOfMagic = size+1
            break
    if lenOfMagic!=1:
        break

print(lenOfMagic)
        
            
