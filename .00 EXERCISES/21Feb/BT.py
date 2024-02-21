s = list(input())

c=[]
for i in range(len(s)):
    if s[i] == '(': c.append(1)
    elif s[i] == ')': c.append(-1)
    elif s[i] == '[': c.append(2)
    elif s[i] == ']': c.append(-2)
    elif s[i] == '{': c.append(3)
    elif s[i] == '}': c.append(-3)

print(c)