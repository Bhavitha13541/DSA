matrix = [[1,1,1],[1,2,1],[1,1,1]]
print(matrix)
row = len(matrix)
col = len(matrix[0])
for i in range(row):
    for j in range(col):
        matrix[i][j] = -1
print(matrix)

# # output:
# [[1, 1, 1], [1, 2, 1], [1, 1, 1]]
# [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

matrix = [[1,1,1],[1,0,1],[1,1,1]]
row = len(matrix)
col = len(matrix[0])
zerorow = [-1] * row
zerocol = [-1] * col
for i in range(row):
    for j in range(col):
        if matrix[i][j] == 0:
            zerorow[i] = 0
            zerocol[j] = 0
for i in range(row):
    for j in range(col):
        if zerorow[i] == 0 or zerocol[j] == 0:
            matrix[i][j] = 0
print(matrix)

# output:
# [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
