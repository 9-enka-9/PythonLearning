import sys
sys.stdin = open("BAI2.INP", "r")

s = input()
for i in s:
    if i == "1":
        print("AX", end="")
    elif i == "3":
        print("AG", end="")
    elif i == "2":
        print("AT", end="")
    else:
        print(i, end = "")
