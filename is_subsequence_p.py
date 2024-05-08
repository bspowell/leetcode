# Have two pointers, one anchor and one runner
# Increment the anchor pointer if the runner equals the letter
# if not, increment the runner


def isSubsequence(s, t):
    left = 0
    right = 0
    if s == '' and len(t) >= 0: return True
    if len(s) > len(t): return False

    while right < len(t):
        if s[left] == t[right]: 
            left += 1
        if left > (len(s) - 1):
            return True
        right += 1
    return False



print(isSubsequence('abc', 'ahbgdc')) # true
print(isSubsequence('axc', 'ahbgdc')) # false
