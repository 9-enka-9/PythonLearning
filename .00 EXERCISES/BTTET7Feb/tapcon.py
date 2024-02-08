n = int(input())
arr = list(map(int,input().split()))

# def f(n, a, i, subset):
#     if i == n:
#         if len(subset)>0:
#             print("{"+ ",".join(map(str, subset)) +"}")
#         return subset
#     subset.append(a[i])
#     f(n, a, i+1, subset)
#     subset.pop()
#     f(n, a, i+1, subset)

# def generate(n, arr):
#     subset = []
#     for i in range(n+1):
#         subset = f(0, arr, i, subset)

# generate(n,arr)
    





# def subsets(arr, n, start, output):
#     if start == n:
#         if len(output) > 0:
#             print("{" + ','.join(map(str, output)) + "}")
#         return
    
#     subsets(arr, n, start + 1, output)  # Không bao gồm phần tử ở vị trí start
#     output.append(arr[start])           # Bao gồm phần tử ở vị trí start
#     subsets(arr, n, start + 1, output)
#     output.pop()                        # Backtracking

# # Đọc dữ liệu vào từ người dùng
# n = int(input())
# arr = list(map(int, input().split()))

# # Gọi hàm subsets để in các tập con
# subsets(arr, n, 0, [])




def generate(a, b, vt, dd):
    if dd==0 and len(b)>0:
        print("{", end="")
        for i in range (len(b)):
            print(b[i], end="")
            if i!=len(b)-1:
                print(",", end="")
        print("}")
        return
    if vt == len(a): 
        return
    b.append(a[vt])
    generate(a,b,vt+1,dd-1)
    b.pop()
    generate(a,b,vt+1,dd)

b=[]
for i in range(n+1):
    generate(arr,b,0,i)