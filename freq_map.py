nums = [1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,7,8,9]

# freq_map = {}
# for i in range(0, len(nums)):
#     if nums[i] in freq_map:
#         freq_map[nums[i]] += 1
#     else:
#         freq_map[nums[i]] = 1

# print(freq_map)

hash_map = {}
for i in range(0, len(nums)):
    hash_map[nums[i]] = hash_map.get(nums[i], 0)+1
print(hash_map)