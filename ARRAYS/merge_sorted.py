nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
res = [x for x in nums1 if x!= 0]
print(res)
        
res1 = [y for y in nums2 if y != 0]
print(res1)
        
res3 = res + res1
print(res3)