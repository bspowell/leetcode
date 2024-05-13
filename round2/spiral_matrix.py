# Left pointer, right pointer, top pointer, bottom pointer
# if left < right
#   for i in range(len(current array))
#       add element from current array
# top += 1
# if top < bottom
#   for i in range(len(matrix))
#       add element from each array[right value]
# right -= 1
# if right > left
#   for i in range(len(bottom array) -1, -1, -1)
#       add element from 1 element over from right
# if top < bottom
#   for i in range(matrix)
#       add element from each array[left value]
# bottom -= 1


def spiralOrder(matrix):
    left, right = 0, len(matrix[0]) - 1
    top, bottom = 0, len(matrix) - 1
    result = []

    while len(result) < (len(matrix) * len(matrix[0])):
        if left == right:
            result.append(matrix[top][right])         

        if left < right:
            for i in range(len(matrix[top])):
                if i >= left and i <= right:
                    result.append(matrix[top][i])

        if top < bottom:
            for i in range(len(matrix)):
                if top != i:
                    result.append(matrix[i][right])
        top += 1
        right -= 1
        if not (left < right and top < bottom): 
            break
        if left < right:
            for i in range(len(matrix[bottom]), -1, -1):
                if i <= right:
                    result.append(matrix[bottom][i])

        if top < bottom:
            for i in range(len(matrix) - 1, -1, -1):
                if i != bottom and i >= top:
                    result.append(matrix[i][left])
        left += 1
        bottom -= 1
  
    return result

    #   print(result)
    #     print('left', left)
    #     print('right', right)
    #     print('top', top)
    #     print('bottom', bottom)
# print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
# print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]
print(spiralOrder([[6,9,7]])) 