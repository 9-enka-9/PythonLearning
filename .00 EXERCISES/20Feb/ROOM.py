import sys, copy

n, m = map(int, input().split())
a = list(map(int, input().split()))
rooms = [0 for i in range(n)]
index = 0

def guestComing(rooms, i):
    global index, a
    originalIndex = index
    originalRooms = copy.deepcopy(rooms)
    while sum(rooms)<n*2 and a[i]>0:
        rooms[index] += 1
        a[i]-=1
        if rooms[index]==2:
            index += 1
    if a[i] != 0:
        index = originalIndex
        rooms = copy.deepcopy(originalRooms)
        return rooms, index
    return 
    

for i in range(m):
    isRun = guestComing(rooms, i)
    if isRun:
        rooms, index = isRun
    if not isRun and rooms[index]:
        index += 1
    if index>=n:
        index=0

for i in range(n):
    print(rooms[i], end=" ")