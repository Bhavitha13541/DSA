nums = [1,2,3,4,5]
k = 2
count = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if sum(nums[i:j + 1]) == k:
            count += 1
print(count)

# output:
# 1