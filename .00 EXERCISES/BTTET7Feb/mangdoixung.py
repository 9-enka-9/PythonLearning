def doixung(a, b, i, j):
  if j == -1:
    return 1
  if a[i] != b[j]:
    return 0
  return doixung(a, b, i + 1, j - 1)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(doixung(a, b, 0, n - 1))
