import sys
sys.stdin = open("WORD.INP", 'r')
sys.stdout = open("WORD.OUT", 'w')

s = input().split()

print(len(s))
for word in s:
    print(word)