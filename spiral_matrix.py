# Given an m x n matrix, return all elements of the matrix in spiral order.

# Examples:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
# Output: [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

# move 4 times in the array
# move 4 times

# Pointer at first array, pointer at last array
# Start at first pointer, put all numbers in new array
# move pointer forward 1 (second array)
# then add last number from each array until second pointer (at the end)
# once you reach second pointer, all all numbers in reverse order
# move last pointer backward 1 (2nd last array)
# add first index of each array until first pointer
# then add all numbers left (without adding already added numbers)
# then move pointer to meet last pointer
# then all first numbers in middle arrays


def sprialMatrix(matrix):
    result = []
    
    if not matrix or not matrix[0]: 
        return result
    
    m, n = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, m - 1, 0, n - 1

    while top <= bottom and left <= right:
        #traverse right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        
        top += 1

        #traverse down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        
        right -= 1

        # traverse left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            
            bottom -= 1
        
        # traverse up 
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result



print(sprialMatrix([[1,2,3],[4,5,6],[7,8,9]]))

