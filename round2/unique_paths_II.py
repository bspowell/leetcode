def uniquePathsWithObstacle(grid):
    rows = len(grid) - 1
    cols = len(grid[0]) - 1

    cache = {}

    def helper(row, col):
        # if row or col is less than 0, or grid has an obstacle, return 0
        if row < 0 or col < 0 or grid[row][col] == 1:
            return 0

        # if we get to last row and col
        if row == 0 and col == 0:
            return 1

        # if row, col is a key in cache, return it
        if (row, col) in cache:
            return cache[(row, col)]
        
        # get sum of left and top element and store as row, col in cache
        result = helper(row, col - 1) + helper(row - 1, col)
        cache[(row, col)] = result
        return result

    return helper(rows, cols)




print(uniquePathsWithObstacle([[0,0,0],[0,1,0],[0,0,0]]))