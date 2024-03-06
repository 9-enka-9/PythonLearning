import sys
sys.stdin = open("BAI3.INP", "r")
sys.stdout = open("BAI3.OUT", "w")

n = int(input())
a = []
for i in range(n):
    t = input()
    a.append(t)

for i in range(n):
    dic = {}
    exist = []
    c = 0
    for j in range(len(a[i])):
        if dic.get(a[i][j]) != None:
            dic.pop(a[i][j])
            exist.append(a[i][j])
        elif a[i][j] not in exist:
            dic[a[i][j]]=j
    if dic != {}:
        for j in dic.keys():
            print(dic[j]+1)
            break
    else:
        print(-1)
