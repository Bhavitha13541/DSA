def reverse_pairs(nums):
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums, 0
        left , count_left = merge_sort(nums[:len(nums) // 2])
        right, count_right = merge_sort(nums[len(nums) // 2:])
        count = count_left + count_right
        j = 0

        # reverse pair count
        for i in range(len(left)):
            while j < len(right) and left[i] > 2 * right[j]:
                j += 1
            count += j

        # merge the two sorted halves
        i = 0
        j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            
            # remaining elements in left or right
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result, count
    _, count = merge_sort(nums)
    return count
nums = [12,2,3,4,5,6,1,0,34,45,50,23,14,17,19,6]
print(reverse_pairs(nums))


# output:
# 31