import itertools, sys

sys.stdin = open("Itertools.out", "w")

arr = [1,2,3]
for item in list(itertools.permutations(arr)):
    print(item)
