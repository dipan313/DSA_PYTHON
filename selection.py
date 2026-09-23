lis = [1,2,3,8,9,5,0]
def selec(lis):
    for i in range(0, len(lis)):
        last = i
        for j in range(i+1,len(lis)):
            if lis[j]<lis[last]:
                last = j
        lis[i],lis[last]=lis[last],lis[i]
selec(lis)
print(lis)
