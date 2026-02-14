nums = [4,5,6,4]
dict = {}
for num in nums:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1
    if dict[num] >= len(nums) // 2:
        print("the majority element is: ", num)
        
# # output:
#  the majority element is:  4

def majorityElement(nums):
    dict = {}
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
        if dict[num] >= len(nums) // 2:
            return num
nums = [2,2,2,4,5,6,7]
print("the majority element is : ",majorityElement(nums))

# output:
# the majority element is :  2