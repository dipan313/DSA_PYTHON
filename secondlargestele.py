lis = [2,5,8,9,-99,99,99999999999]
large=float("-inf")
slar=float("-inf")
# print(large)
# for i in range (0, len(lis)):
#     large = max(lis[i],large)
# print(large)
# for i in range (0, len(lis)):
#     if lis[i] < large:
#         slar = max(lis[i],slar)
# print(slar)

for i in range(0, len(lis)):
    if lis[i]>large:
        slar = large
        large = lis[i]
print(large)
print(slar)