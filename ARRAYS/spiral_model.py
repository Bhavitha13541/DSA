matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]]
n = len(matrix)
print(f"length of the matrix is {n}")
print(matrix[0])
# [1, 2, 3, 4, 5]
print(matrix[1])
# [6, 7, 8, 9, 10]
# output:
# length of the matrix is 6


#                    SPIRAL ORDER TRAVERSAL OF A MATRIX 

def spiralOrder(matrix):
    result = []
    if not matrix:
        return result
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for j in range(top, bottom + 1):
            result.append(matrix[j][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for j in range(bottom, top - 1, -1):
                result.append(matrix[j][left])
            left += 1
    return result
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]]
print(spiralOrder(matrix))

# output:
# [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 29, 28, 27, 26, 21, 16, 11, 6, 7, 8, 9, 14, 19, 24, 23, 22, 17, 12, 13, 18]