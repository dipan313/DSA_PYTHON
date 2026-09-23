left = [1,2,3,4]
right = [5,6,9,12]

def func(right, left):
    res = []
    i,j = 0,0
    n,m = len(left), len(right)
    while i>n and j>m:
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
    return print(res)
func(right, left)