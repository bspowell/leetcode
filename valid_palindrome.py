#Algo
# Have two pointers start at beginning and end
# check each one is the same. 
# If one is not the same
#   check count is still at 0
#       Delete the one 
#       add + 1 to count
#   if not 0, then not a valid palindrome


def validPalindrome(s):
    left = 0
    right = len(s) - 1

    def check_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return check_palindrome(left + 1, right) or check_palindrome(left, right - 1)
    return True


# Alternative: using strings, and creating 
# Time Complexity: O(N)
# The while loop iterates approximately n/2 times, where n is the length of the input string s.
# Space Complexity: O(N) - once for each string, then once for the reverse
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#             p1 = 0
#             p2 = len(s)-1
#             while p1 <= p2:
#                 if s[p1] != s[p2]:
#                     string1 = s[:p1] + s[p1+1:]
#                     string2 = s[:p2] + s[p2+1:]
#                     return string1 == string1[::-1] or string2 == string2[::-1]
#                 p1 += 1
#                 p2 -= 1
#             return True




print(validPalindrome('abc'))
print(validPalindrome('abbca'))
print(validPalindrome('abc')) 
print(validPalindrome('eccer'))

# print(check_palindrome('abc'))
# print(check_palindrome('abba'))
# print(check_palindrome('aba'))

