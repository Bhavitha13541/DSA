#                        THIS IS USING FOR LOOPS

nums = [1,2,3]
sub_arrays = []
for i in range(len(nums)):
    for j in range(i, len(nums)):
        sub_arrays1 = sub_arrays.append(nums[i:j+1])
        print(nums[i:j+1])
print("The list of sub arrays are: ", sub_arrays)

# output:
# [1]
# [1, 2]
# [1, 2, 3]
# [2]
# [2, 3]
# [3]
# The list of sub arrays are:  [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]

sums = [[1], [1,2], [1,2,3]]
sum_of_sub_arrays = []
for num in sums:
    print(sum(num))
    sum_of_sub_arrays.append(sum(num))
print("the list of sum of sub arrays is :",sum_of_sub_arrays)
print("the max sum of sub arrays is : ",max(sum_of_sub_arrays))

# ouput:
# 1
# 3
# 6
# the list of sum of sub arrays is : [1, 3, 6]
# the max sum of sub arrays is :  6

def maxSubArray(nums):
    list_of_sub_arrays = []
    sum_of_sub_arrays = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            list_of_sub_arrays.append(nums[i:j+1])
            for num in list_of_sub_arrays:
                sum_of_sub_arrays.append(sum(num))
        return max(sum_of_sub_arrays)
# nums = [-3,0,6,-6,-4,8,-29,7,-4,24]
# print("the max sum of sub arrays is : ", maxSubArray(nums))

# output:
# the max sum of sub arrays is :  -3

#            USING LIST COMPREHENSION 
nums = [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
sum_of_sub_arrays = [sum(num) for num in nums]
print("the list of sum of sub arrays is : ", sum_of_sub_arrays)
print("the max sum of sub arrays is : ", max(sum_of_sub_arrays))

# output:
# the list of sum of sub arrays is :  [1, 3, 6, 2, 5, 3]
# the max sum of sub arrays is :  6