def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a-1)

with open('BAI1.INP', 'r') as input_file:
    n = int(input_file.read().strip())

s = 0
for i in range(1,n+1):
    if i % 2 == 0:
        s -= factorial(i)
    else:
        s += factorial(i)
    
print(s)

with open('BAI1.OUT', 'w') as output_file:
    output_file.write(str(s))