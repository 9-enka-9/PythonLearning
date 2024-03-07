n, m = map(int, input().split())
a = []

# à cái mảng hai chiều e nhập được rồi, cái đó là hình như là mấy số [0]*n như vậy hình như nó hiểu bản chất là 1 á, nên nó thay đổi 1 cái là thay đổi hết lun
for i in range(n):
    t = []
    for j in range(n):
        t.append(0)
    a.append(t)

for i in range(m):
    x, y = map(int, input().split())
    a[x][y]=1
    a[y][x]=1

for j in range(n):
    print(a[j])