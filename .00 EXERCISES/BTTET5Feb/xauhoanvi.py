s1 = input().lower()
s2 = input().lower()

# def toDict(s):
#     chars = {}
#     for char in s:
#         isDifferent = True
#         for i in chars:
#             if char == i:
#                 chars[char]+=1
#                 isDifferent = False
#                 break
#         if isDifferent:
#             chars[char] = 0
#     return chars


# dict1 = toDict(s1)
# dict2 = toDict(s2)

# if dict1 == dict2:
#     print(1)
# else:
#     print(0)






# ANOTHER WAY FROM DI: sort(s1.lower), sort(s2.lower) -> check if s1 == s1: print(1) else: print(0)  
s1 = list(s1)
s2 = list(s2)
s1.sort()
s2.sort()
if s1 == s2:
    print(1)
else:
    print(0)