import math
triangle = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1]
]
n = 5
k = 3
num = math.factorial(n - 1) // (math.factorial(k - 1) * math.factorial(n - k))
print("the element at 6 row and 3 column is : ", num)

print("the entire 6th row is :", triangle[n - 1])

# the entire 6th row is : [1, 5, 10, 10, 5, 1]
# output:
# the element at 6 row and 3 column is :  10

#  for getting entire row we can alse use the formula

import math 
rows = [math.comb(n, k) for k in range(n + 1)]
print("the entire 6thh row is : ", rows)

# the entire 6thh row is :  [1, 5, 10, 10, 5, 1]

import math

n = 6
for i in range(n):
    row = [math.comb(i, k) for k in range(i + 1)]
    print(row)

# output:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]