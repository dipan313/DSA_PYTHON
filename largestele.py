lis = [2,5,8,9,-99,99,99999999999]
large = lis[0]
for i in lis:
    # if i>large:
    #     large = i
    large = max(large,i)
print(large)