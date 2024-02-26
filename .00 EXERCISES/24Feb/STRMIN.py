n = int(input())
x, y, z = map(int, input().split())
# x: hoa, y: thuong, z: so
s = ''
hoa = 'A'
thuong = 'a'
so = '0'
for i in range(z):
    s += so
    if so < '9':
        so = chr(ord(so)+1)
    else:
        so = '0'

for i in range(x):
    s += hoa
    if hoa < 'Z':
        hoa = chr(ord(hoa) + 1)
    else:
        hoa = 'A'

for i in range(y):
    s += thuong
    if thuong < 'z':
        thuong = chr(ord(thuong) + 1)
    else:
        thuong = 'a'

print(s)
