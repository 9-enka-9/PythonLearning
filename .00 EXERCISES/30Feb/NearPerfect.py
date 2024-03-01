import sys

l = int(input())
d = int(input())

def tonguoc(num):
    if num == 1: return 0
    s=1
    for i in range(2, int(num**0.5)+1):
        if num % i==0 and num//i!=i:
            s+=i+num//i
            continue
        if num % i==0:
            s+=i
    return s

c=0
for num in range(1,l):
    if abs(num - tonguoc(num)) <= d:
        c+=1

print(c)
