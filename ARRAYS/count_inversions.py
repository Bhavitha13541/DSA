# brute force solution

nums = [2,3,7,1,3,5]
count = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] > nums[j] and i < j:
            count += 1

print(count)

# output:5