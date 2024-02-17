n = int(input())
a = list(map(int, input().split()))
a.sort()

count = 0
current = 0
for x in a:
    if current + x <= 4:
        current += x
    else:
        count += 1
        current = x

print(count + (current != 0))