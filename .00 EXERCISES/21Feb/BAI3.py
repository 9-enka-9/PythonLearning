s1 = input().lower()
s2 = input().lower()

check = True
for i in range(len(s1)):
    if s1[i] not in s2:
        check = False
        break

if check:
    print('YES')
else:
    print('NO')