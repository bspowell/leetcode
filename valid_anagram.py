# Given two strings s and t, return true if t is an anagram of s, 
# and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


# sorting algorithms - O(N log N) time complexity 
# Should be able to iterate over string once - O(N)

# put first string into a hash with letters as true
# then iterate over second string to check if each letter is within the hash, if not return false


def valid_ana(s, t):

  if len(s) != len(t): return False

  new_hash = {}
  for letter in s:
    if new_hash.get(letter):
      new_hash[letter] += 1
    else: 
      new_hash[letter] = 1
      
  for lett in t:
    if new_hash.get(lett):
      new_hash[lett] -= 1
    else:
      return False
  return True


print(valid_ana("anagram","nagaram"))
print(valid_ana("rat","car"))
print(valid_ana("anagram","nagaramdffd"))
print(valid_ana("anagram","aram"))
print(valid_ana("aacc","ccac"))
print()