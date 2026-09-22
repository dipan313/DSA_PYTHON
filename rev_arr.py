lis = [1,2,3,4,5,6,7,8,9]
left  = 0
right = len(lis)-1

def func(lis, left, right):
    if left>=right:
        return
    lis[left],lis[right]=lis[right],lis[left]
    func(lis, left+1, right-1)
func(lis, left, right)
print(lis)
