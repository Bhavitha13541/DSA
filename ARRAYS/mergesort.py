# def merge_sort(arr1):
#     if len(arr1) <= 1:
#         return arr1
#     print(arr1, "merge")
#     left = merge_sort(arr1[:len(arr1) // 2])
#     right = merge_sort(arr1[len(arr1) // 2:])
    

# arr1 = [2,34,45,5,1,10,34,98]
# print(merge_sort(arr1))


def merge_Sort(nums):
    if len(nums) <= 1:
        return nums
    print(nums, "nums")
    left = merge_Sort(nums[:len(nums)//2])
    print(left, "left")
    right = merge_Sort(nums[len(nums)//2:])
    print(right, "right")

    i = 0
    j = 0
    result = []
    while i < len(left) and  j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


nums = [2,5,6,1,0,12,14,13,11,15,19,16,7]
print(merge_Sort(nums))

# output:
# [0, 1, 2, 5, 6, 7, 11, 12, 13, 14, 15, 16, 19]