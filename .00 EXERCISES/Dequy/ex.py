
# arr = list(map(int, input().split()))

def tong(n, arr):
    if n==0:
        return 0
    return arr[n-1] + tong(n-1, arr)


def timmax(n, arr):
    if n==0:
        return arr[0]
    return max(timmax(n-1,arr), arr[n-1])

n = int(input())
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)

print(fibo(n))