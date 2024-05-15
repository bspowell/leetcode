def longestCommonSubsequence(text1, text2):

    str1 = len(text1)
    str2 = len(text2)
    minPoint = 0
    maxCount = 0
    start = 0

    if str1 > str2:
        while minPoint < str2 - 1:
            count = 0
            for i in range(start, str1):
                if text1[i] == text2[minPoint]:
                    minPoint += 1
                    count += 1
                    print('i', i)
                    print('minPoint', minPoint)
                    print('count', count)
            if minPoint == 0:
                minPoint += 1

            minPoint += 1
            i + 1

    else:
        for i in range(str2):
            if text2[i] == text1[minPoint]:
                minPoint += 1
                count += 1

    return count

print(longestCommonSubsequence("abcde", "ace"))
print(longestCommonSubsequence("abc", "def"))
print(longestCommonSubsequence("bl", "yby"))
print(longestCommonSubsequence("psnw", "vozsh"))