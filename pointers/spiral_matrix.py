# Given an m x n matrix, return all elements of the matrix in spiral order.

# Examples:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
# Output: [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

def sprialMatrix(matrix):
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # get every i in the top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1 #shift pointer down by 1

        # get every i in the right col
        for i in range(top, bottom):
            res.append(matrix[i][right - 1]) # subtract by 1, since it's out of bounds
        right -= 1 # shift pointer left by 1

        # if pointers have crossed, break out. eg. single row matrix
        if not (left < right and top < bottom): 
            break

        # going from right to left in reverse order
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1 # shift pointer up by 1

        # get every i in the left col
        for i in range(bottom - 1, top - 1, - 1):
            res.append(matrix[i][left])
        left += 1 # shifting pointer to the right by 1
        
    return res
        


print(sprialMatrix([[1,2,3],[4,5,6],[7,8,9]]))

