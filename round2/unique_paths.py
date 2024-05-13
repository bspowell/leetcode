def uniquePaths(rows, cols):
    
    def helper(rows, cols, cache):
        if rows == 1 or cols == 1:
            return 1

        if (rows, cols) not in cache:
            cache[(rows, cols)] = helper(rows - 1, cols, cache) + helper(rows, cols - 1, cache)
        
        return cache[(rows, cols)]

    return helper(rows, cols, {})

print(uniquePaths(3, 7)) # 28
print(uniquePaths(3, 4)) # 28