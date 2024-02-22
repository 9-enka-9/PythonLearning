s = input()

check = True
c = [0]
index = 0
for i in range(len(s)):
    if s[i] == '(':
        c.append(1)
    elif s[i] == '[':
        c.append(2)
    elif s[i] == '{':
        c.append(3)
    elif s[i] == ')':
        if c[len(c)-1] == 1:
            c.pop()
        else:
            check = False
            break
    elif s[i] == ']':
        if c[len(c)-1] == 2:
            c.pop()
        else:
            check = False
            break
    elif s[i] == '}':
        if c[len(c)-1] == 3:
            c.pop()
        else:
            check = False
            break

if check and c == [0]:
    print("YES")
else:
    print("NO")