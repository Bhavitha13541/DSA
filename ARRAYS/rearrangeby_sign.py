nums = [3,4,-1,-6,7,-2,5,-8]
pos = []
neg = []
for num in nums:
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)
# print("the rearranged array is : ", pos + neg)

# # output:
# # the rearranged array is :  [3, 4, 7, 5, -1, -6, -2, -8]
i = 0
while 2* i < len(nums):
    nums[2*i] = pos[i]
    nums[2*i + 1] = neg[i]
    i += 1
print("the rearranged array is with a alternating sign is : ", nums)
# output:
# the rearranged array is with a alternating sign is :  [3, -1, 4, -6, 7, -2, 5, -8]