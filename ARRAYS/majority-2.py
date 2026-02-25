nums = [1,1,1,3,3,2,2,2]
F = {}
L = []
for num in nums:
    if num in F:
        F[num] += 1
    else:
        F[num] = 1

for num in F:
    if F[num] > len(nums) // 3:
        L.append(num)

print(L)
        

# output:
# {3: 4, 1: 1, 2: 1, 5: 1, 4: 2}
