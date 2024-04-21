

def strStr(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1



print(strStr('sadbutsad', 'sad'))
print(strStr('leetcode', 'leeto'))

# Time Complexity: O(m * n)
# Space Complexity: O(1)