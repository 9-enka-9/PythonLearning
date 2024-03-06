import sys
sys.stdin = open("BAI2.INP", "r")
sys.stdout = open("BAI2.OUT", "w")

s = input()
prime = [False, False, True, True, False, True, False, True, False, False]
res = []
for i in s:
    if i in res:
        continue
    if prime[int(i)]:
        res.append(i)
        print(i)
