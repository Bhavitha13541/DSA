def peak_element(num):
    if len(num) == 1:
        return 0, num[0]
    if num[0] > num[1]:
        return 0, num[0]
    if num[len(num) - 1] > num[len(num) - 2]:
        return len(num) - 1, num[len(num) - 1]
    low = 1
    high = len(num) - 2
    while low <= high:
        mid = (low + high) // 2
        if num[mid] > num[mid - 1] and num[mid] > num[mid + 1]:
            return mid, num[mid]
        elif num[mid] > num[mid - 1]:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, None
nums = [1,2,3,1,2,3,1]
index, value = peak_element(nums)
print(f"Peak element is {value} at index {index}")


# output: Peak element is 3 at index 2
        
    
