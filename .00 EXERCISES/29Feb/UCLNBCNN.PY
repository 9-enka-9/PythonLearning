import sys
from math import gcd
sys.stdin = open("UCLNBCNN.inp", "r")

a,b = map(int, input().split())

ucln = gcd(a,b)
bcnn = (a*b)//ucln
print(ucln,bcnn)
