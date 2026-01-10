def union_array(arr1, arr2):
    union_set = []
    for x in arr1:
        if x not in union_set:
            union_set.append(x)
    for y in arr2:
        if y not in union_set:
            union_set.append(y)
    return union_set

arr1 = [1,2,3,4,4]
arr2 = [3,4,5,6]
result = union_array(arr1, arr2)
print("Union of two arrays is: ", result)

# output:
# Union of two arrays is:  [1, 2, 3, 4, 5, 6]