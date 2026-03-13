#  USING LOWER BOUND TECHNIQUE

def search_insert(nums, target):
    low = 0
    high = len(nums) - 1
    ans = len(nums) 
    # if target is grater than all elements in the array, it should be inserted at the end of the array, which is at index len(nums)
    while high >= low:
        mid = (low + high) // 2
        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
nums = [1,2,3,4,5,6,8,9,9,9,10]
target = 7
result = search_insert(nums, target)
print(f"Element should be inserted at index: {result}")

# output: Element should be inserted at index: 6

# USING UPPER BOUND TECHNIQUE

def search_insert(nums, target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)
    while high >= low:
        mid = (low + high) // 2
        if nums[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

nums = [1,2,3,4,5,6,8,9,9,9,10]
target = 8
result = search_insert(nums, target)
print(f"Element should be inserted at index: {result}")

# output: Element should be inserted at index: 7