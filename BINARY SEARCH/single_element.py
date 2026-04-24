#    BRUTE FORCE APPROACH

nums = [1,1,2,2,3,3,4,5,5,6,6]
def single_element(nums):
    for i in range(len(nums)):
        if i == 0 and nums[i] != nums[i + 1]:
            return nums[i]
        elif i == len(nums) - 1 and nums[i] != nums[i -1]:
            return nums[i]
        elif nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
            return nums[i]
    return None

print(single_element(nums))


#  OPTIMIZED APPROACH 


nums = [1,1,2,2,3,3,4,4,5,5,6,7,7,8,8]
def single_elements(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n - 1] != nums[n - 2]:
        return nums[n - 1]
    low = 1
    high = n- 2
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        elif (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid - 1]):
            low = mid + 1
        else:
            high = mid - 1
    return None


print("single element is : '", single_elements(nums), "'")

# single element is : ' 6 '