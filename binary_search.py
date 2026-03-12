                #    THIS IS USING BINARY SEARCH

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while high >= low:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

nums = [1,3,5,7,9,11,13]
target = 7
result = binary_search(nums, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")

    # output: Element found at index: 3


            #   WITH OUT USING BINARY SEARCH

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

nums = [1,3,5,7,9,11,13]
target = 4
result = linear_search(nums, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")

    # output: Element not found in the array