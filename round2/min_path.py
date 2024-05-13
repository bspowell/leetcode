def minPath(grid):
    rows = len(grid) - 1
    cols = len(grid[0]) - 1

    def helper(row, col):
        
        # if row or col < 0, return infinity so it always chooses the other column
        if row < 0 or col < 0:
            return float('inf')

        # return final row and col
        if row == 0 and col == 0:
            return grid[0][0]

        # return current grid val + min from either left or up
        result = grid[row][col] + min(helper(row - 1, col), helper(row, col - 1))

        return result


    return helper(rows, cols)


print(minPath([[1,3,1],[1,5,1],[4,2,1]])) 
print(minPath([[1,2,3],[4,5,6]])) 