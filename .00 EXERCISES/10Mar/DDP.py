def count_palindrome(matrix):
  global n
  dp = [[0] * n for _ in range(n)]
  is_palindrome = [[False] * n for _ in range(n)]

  # Khởi tạo
  for i in range(n):
    for j in range(n):
      is_palindrome[i][j] = matrix[i][j] == matrix[n - 1 - j][n - 1 - i]
      if i == n - 1 or j == n - 1:
        dp[i][j] = 1 if is_palindrome[i][j] else 0

  # Duyệt từ dưới lên trên, từ trái sang phải
  for i in range(n - 2, -1, -1):
    for j in range(n - 2, -1, -1):
      if is_palindrome[i][j]:
        dp[i][j] = dp[i + 1][j + 1] + 1
        if matrix[i][j] == matrix[i + 1][j]:
          dp[i][j] += dp[i + 1][j]
        if matrix[i][j] == matrix[i][j + 1]:
          dp[i][j] += dp[i][j + 1]

  return dp[0][0]


import sys
sys.stdin = open("DDP.INP", "r")

n = int(input())
a = []
for i in range(n):
    a.append(list(input().split()))

print(count_palindrome(a))

