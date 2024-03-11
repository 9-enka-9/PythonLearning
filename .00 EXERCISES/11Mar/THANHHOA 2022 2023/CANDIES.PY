import sys
sys.stdin = open("CANDIES.INP", "r")
sys.stdout = open("CANDIES.OUT", "w")

n = int(input())
a = list(map(int, input().split()))

s=0
c=0
for i in range(n):
    if a[i]>0 and a[i]%3 == 0:
        s+=a[i]
        c+=1

print(c)
print((s - c*3)//3)
