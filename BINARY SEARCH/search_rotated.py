def search_rotated(nums, target):
    n = len(nums)
    target = target % n
    return nums[target:] + nums[:target]
nums = [4,5,6,7,0,3,1,2]
target = 3
print(f"Rotated array: {search_rotated(nums, target)}")
low = 0
high = len(nums) - 1
while high >= low:
    mid = (low + high) // 2
    if nums[mid] == target:
        print(f"Target {target} found at index: {mid}")
        break
    elif nums[mid] >= nums[low]:
        if nums[low] <= target <= nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        if nums[mid] <= target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1
else:
    print(f"Target {target} not found in the array.")

# output:
# Rotated array: [7, 0, 3, 1, 2, 4, 5, 6]
# Target 3 found at index: 5
