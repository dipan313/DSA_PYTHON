n = [1,2,2,2,2,3,3]
m = [1,2,3,4,5]
# dict = {}
# for i in range (0, len(n)):
#     count = 0
#     for j in range (0, len(m)):
#         if m[j]<=9 and m[j]>=1:
#             if n[i] == m[j]:
#                 count += 1
#             dict[n[i]] = count
# print(dict)

# hash_list = [0] * 11
# print(hash_list)
# for i in n:
#     hash_list[i] +=1
# print (hash_list)

# for j in m:
#     if j<=9 and j>=1:
#         print(j, '=', hash_list[j])
#     else:
#         print(j,'= 0')

dict = {}
print(type(dict))

for i in n:
    if i in dict:
        dict[i] +=1
    else:
        dict[i] = 1
print(dict)
