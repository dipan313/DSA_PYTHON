lis = [1,2,5,6,9,8,7]
res = True
for i in range(0, len(lis)-1):
    if lis[i] < lis[i+1]:
        res = True
    else:
        res = False

print(res)