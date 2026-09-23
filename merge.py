arr = [8,9,4,5,6,1,2,35,5,9,3,12]

def merge(left, right):
    res = []
    i,j = 0,0
    n,m = len(left), len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    if i<n:
        while i<n:
            res.append(left[i])
            i+=1
    if j<m:
        while j<m:
            res.append(right[j])
            j+=1
    return res

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
print(merge_sort(arr))