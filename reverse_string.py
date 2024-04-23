# Best case scenario for memory would be by doing an in-place mutation costing 0(1) memory
# Best case for time complexity would be only iterating over only half the string once, which would be O(N / 2)
# Sorting algos use O(N log N) as the best time. 

#iterate over the string
# for each letter until half, do a swap of the last letter and first letter

def reverseString(s):
    last = -1
    for i in range(len(s) // 2):
      s[i], s[last] = s[last], s[i]
      last -= 1

    return s
        

print(reverseString(['h','e','l','l','o'])) # 'olleh'
print(reverseString(["H","a","n","n","a","h"])) # 'olleh'