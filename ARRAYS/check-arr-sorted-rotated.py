# for a sorted and rotated array have only one break 
# so if 

A = [2,1]
n = len(A)
count = 0
for i in range(n):
  if A[i] > A[(i+1)% n]:
    count += 1
  if count > 1:
    print(False)
print(True)



