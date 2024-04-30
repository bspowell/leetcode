# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j - can't be the same index
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# iterate over the array and create an object with keys as each element doubled, and values as true
# Iterate over the array again, and for each element check the object for the value
# return true if it finds the value, false if not
# Time complexity: Since we are iterating over the array twice, we get O(2N)
# Space Complexity: Since we created a new hash with the same amount that's in the array, it's O(N)

def checkIfExist(arr):
  doubles = {}
  for index in range(len(arr)):
    doubles[arr[index] * 2] = index

  print(doubles)
  
  for index in range(len(arr)):
    index_of_double = doubles.get(arr[index])
    if isinstance(index_of_double, int) and (index_of_double != index):
      return True
    
  return False



print(checkIfExist([10,2,5,3]))
print(checkIfExist([3,1,7,11])) 
print(checkIfExist([-2,0,10,-19,4,6,-8]))
print(checkIfExist([0,0]))
print(checkIfExist([7,1,14,11]))




