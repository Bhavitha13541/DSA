#  BRUTE FORCE SOLUTION

nums = [2,3,0,-2,4,1]
def max_product(nums):
    if not nums:
        return 0
    max_product = nums[0]
    for i in range(len(nums)):
        pro = 1
        for j in range(i, len(nums)):
            pro *= nums[j]
            if pro > max_product:
                max_product = pro
    return max_product

print(max_product(nums))

# output: 6

# optimal solution
nums = [2,3,0,-2,4,1]
def maxProduct(nums):
        max_p = nums[0]
        min_p = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            temp = max(num, max_p * num, min_p * num)
            min_p = min(num, max_p * num, min_p * num)
            max_p = temp
            
            if max_p > res:
                res = temp
        return res
print(maxProduct(nums))

# output: 6