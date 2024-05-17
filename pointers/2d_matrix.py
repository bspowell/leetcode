# Algo:
# Given a number and an array of arrays 
# If number is less than the last number in the array, interate over that array
# if number is within that array, then return true, false otherwise
# Time Complexity: O(N + M) - iterate through last element of each array then only when
# we find the right array, we look through it. 
# Space complexity: O(1) - didn't create any more space 

def searchMatrix(matrix, target):
    for arr in matrix:
      if arr[-1] >= target:
        if target in arr:
          return True
    return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))


# alt sol: return any(target in row for row in matrix)
