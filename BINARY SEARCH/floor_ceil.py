
def floor(nums, target):
    low = 0
    high = len(nums) - 1
    while high >= low:
        mid = (low + high) // 2
        if nums[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1
    return nums[mid-1],nums[mid]
nums =[3, 4, 4, 7, 8, 10]
target  = 8
result = floor(nums, target)
print(f'Floor and ceiling of {target} is: {result}')

# output: Floor and ceiling of 5 is: (4, 7)