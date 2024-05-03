# Algo: 
# Iterate from 1 to given number and for each increment, multiply the number together
#   if the numbers value equals the given number, then it's a perfect square
#   if the numbers value  is over the given number, then it;s not a perfect square
# 
# Time Complexity: O(N / 2) - binary search would be faster
# Space Complexity: O(1) - didnt' create any more data strucutres except n 


def isPerfectSquare(num):
  n = 1
  while (n * n) <= num:
    if (n * n) == num:
      return True
    n += 1
  return False



print(isPerfectSquare(16)) # true
print(isPerfectSquare(15)) # false
print(isPerfectSquare(2)) # false
print(isPerfectSquare(1)) # true
