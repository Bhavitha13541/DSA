nums = [2,0,2,1,1,0]
for i in range(len(nums)-1, 0, -1):
    for j in range(i):
        if nums[j] > nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
            print(nums)


def sortColors(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums
nums = [2,3,1,4,5,6]
print(sortColors(nums))

# output:
[1, 2, 3, 4, 5, 6]