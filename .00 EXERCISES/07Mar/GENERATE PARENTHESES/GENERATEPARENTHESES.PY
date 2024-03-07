import sys
sys.stdin = open("GENERATEPARENTHESES.INP", "r")

def generate(s):
    global n
    if len(s[0]) == n:
        return s
    L = []
    for paren in s:
        L.append(paren + "(")
        L.append(paren + ")")
    return generate(L)

def isValid(s):
    count = 0
    for c in s:
        if c == "(":
            count +=1
        else:
            if count == 0:
                return False
            else:
                count -=1
    return count == 0

n = int(input())
s = [""]
n = n*2
L = generate(s)

for paren in L:
    if isValid(paren):
        print(paren)

