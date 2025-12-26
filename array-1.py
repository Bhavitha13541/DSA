# 1-Largest Element in an Array
arr = [10, 25, 3, 98, 45]
max_element = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]
print("Largest element is : ", max_element)

# output: Largest element is :  98
# time complexity: O(n)
# space complexity: O(1)

# 2- Smallest Element in an array

arr = [10, 25, 3, 98, 45]
min_element = arr[0]
for i in range(1, len(arr)):
    if arr[i] < min_element:
        min_element = arr[i]
print("Smallest element is : ", min_element)

# output: Smallest element is : 3

# Another approach using built-in function
arr = [34, 65, 67, 27,90, 69,12]
min_element = min(arr)
max_element = max(arr)
print("Smallest element is : ", min_element)
print("Largest element is : ", max_element)

# output:   
# Smallest element is :  12
# Largest element is :  90