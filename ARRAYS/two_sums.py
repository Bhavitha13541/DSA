nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)


# using functions

def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            
nums = [2,7,11,15,20]
target = 9
nums = [3,4,6]
target = 10
result = two_sum(nums,target)
print(result)

# output:
[1, 2]