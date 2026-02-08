# DICTJIONARY 
freq = {1:2, 2:4, 3:1, 4:5}
print(freq[3])
print(freq[2])
print(freq[4])

# # enumarate() will give us the index and the value of the dictionary

for i, num in enumerate(freq):
    print(i, num)
# output:
# 0 1
# 1 2
# 2 3
# 3 4

#    finding shortest subarray with the same degree as the original array
nums = [1,2,2,3,1,4,2]
first = {}
last =  {}
count = {}
for i, num in enumerate(nums):
    if num not in first:
        first[num] = i
    last[num] = i
    count[num] = count.get(num, 0) + 1

degree = max(count.values())

min_length = len(nums)
for num in count:
    if count[num] == degree:
        length = last[num] - first[num] + 1
        min_length = min(min_length, length)
print("the minimum length of the array:",min_length)

# output:
# the minimum length of the array: 6