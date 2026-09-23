arr = [8,9,6,5,7,2,3]
# def bubble(arr):
#     for i in range(0,len(arr)):
#         is_swap=False
#         for j in range(i+1,len(arr)):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j] = arr[j],arr[i]
#                 is_swap= True
#         if is_swap == True:
#             return
def bubble(arr):
    for i in range(len(arr)-2,-1,-1):
        is_swap=False
        for j in range(0, i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                is_swap= True
        if is_swap == True:
            return
bubble(arr)
print(arr)
