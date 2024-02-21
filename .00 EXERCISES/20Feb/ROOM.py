import sys, copy

n, m = map(int, input().split())
a = list(map(int, input().split()))
rooms = [0 for i in range(n)]
index = 0
sRooms = 0
left1 = []

def guestComing(rooms, i):
    global index, a, sRooms
    originalIndex = index
    originalRooms = copy.deepcopy(rooms)
    originalsRooms = sRooms
    originalA = copy.deepcopy(a)
    while sRooms<n*2 and a[i]>0 and index<n:
        rooms[index] += 1
        sRooms += 1
        a[i]-=1
        if rooms[index]==2:
            index += 1
    if a[i] != 0:
        if n*2-sRooms>=a[i]:
            for j in left1:
                if a[i]!=0:
                    rooms[j]+=1
                    a[i]-=1
                    sRooms +=1
                else:
                    break
            index = left1[-1]
        else:
            return originalRooms, originalIndex, originalsRooms, originalA
    

for i in range(m):
    isRun = guestComing(rooms, i)
    if isRun:
        rooms, index, sRooms, a = isRun
    if not isRun and rooms[index]:
        if rooms[index] == 1:
            left1.append(index)
        index += 1

# if index == n:
#     index=0
# if n*2 - sRooms!=0:
#     for i in range(m):
#         if n*2 - sRooms > a[i] and a[i]>0:
#             for j in range(n):
#                 if 2-rooms[j]>0:
#                     rooms[j]+=1
#                     sRooms += 1

for i in range(n):
    print(rooms[i], end=" ")