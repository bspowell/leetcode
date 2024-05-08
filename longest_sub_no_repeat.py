# given a string
# have left pointer at index 0 and right iterate over string
# 1. If letter is in set, remove it, and move left + 1
# 2. Add current letter to set
# 3. Add to result, the max of r-l + 1



def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res


print(lengthOfLongestSubstring('abcabcabc'))
print(lengthOfLongestSubstring('abcdeaa'))
print(lengthOfLongestSubstring(''))
print(lengthOfLongestSubstring('aaaa'))
print(lengthOfLongestSubstring('tmmzuxt'))




