s = "vnjaldfnafncjdmnfvcjkdmhnflcjadshnfcjmdhsnjeoz"
d = ['d', 'e', 'o']
hash_list = [0]*26
print (hash_list)
for ch in s:
    asc = ord(ch)
    ind = asc - 97
    hash_list[ind] +=1
print (hash_list)

for ch in d:
    asc = ord(ch)
    ind = asc -97
    print(hash_list[ind])
