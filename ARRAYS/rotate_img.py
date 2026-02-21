matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
n = len(matrix)
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print(matrix)

# output:
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]] this is the transposed matrix of the original matrix
# matrix.reverse()      this will reverse the order of the rows in the matrix
# print(matrix)
        
for row in matrix:
    row.reverse()
print(matrix)

# output:
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]] this is the rotated image by 90 degree in the clockwise direction

# print(matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j])

#  using functions
def rotateImage(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
        return matrix
matrix = [[1,2,3,4],[5,6,7,8],[0,10,11,12],[13,14,15,16]]
print(rotateImage(matrix))

# ouput:
# [[13, 0, 5, 1], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]