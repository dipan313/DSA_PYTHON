lis = [3,5,4,6,9,1]
n = len(lis)
def ins(lis):
    for i in range(1,n):
        key = lis[i]
        j = i-1
        while j>=0 and lis[j]>key:
            lis[j+1]=lis[j]
            j-=1
        lis[j+1]=key

ins(lis)
print(lis)
