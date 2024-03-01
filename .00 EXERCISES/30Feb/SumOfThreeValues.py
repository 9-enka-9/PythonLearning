import itertools

##n, x = map(int, input().split())
##arr = list(map(int, input().split()))
##index = [i for i in range(n)]
##res =()
##for order in list(itertools.combinations(index,3)):
##    t = sum([arr[order[0]], arr[order[1]], arr[order[2]]])
##    if t==x:
##        res = order
##        break
##if res:
##    print(res[0]+1, res[1]+1, res[2]+1)
##else:
##    print("IMPOSSIBLE")


def find_three_values(n, x, a):
  hash = {}
  for i in range(n):
    hash[a[i]] = i
  for i in range(n):
    for j in range(i + 1, n):
      if x - a[i] - a[j] in hash:
        k = hash[x - a[i] - a[j]]
        if j < k and a[j] + a[i] in hash:
          return i + 1, j + 1, k + 1
  return "IMPOSSIBLE"

n, x = map(int, input().split())
a = list(map(int, input().split()))
result = find_three_values(n, x, a)
if result!="IMPOSSIBLE":
    for i in result:
        print(i,end=" ")
else:
    print(result)
