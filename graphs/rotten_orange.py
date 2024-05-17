def orangesRotting(self, grid):
    fresh, minutes = 0, 0
    rottenq = []
    
    rows, cols = len(grid), len(grid[0])
        
            # Iterate over grid to add rotten orange coordinates + fresh count
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                rottenq.append([row, col])
            if grid[row][col] == 1:
                fresh += 1

    directions = [(1,0), (0,1), (-1, 0), (0, -1)]					
    
    # while there are coordinates
    while rottenq and fresh > 0:
            # iterate length of coordinates list, pop first one, check squares
            # around it to see if rotten, nothing or fresh
        for i in range(len(rottenq)):
            row, col = rottenq.pop(0)
            for dr, dc in directions:
                r, c = row + dr, col + dc
                # if in bounds, and not fresh orange, skip
                if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                    continue
                else:
                # make fresh orange rotten, add new coords to queue
                    grid[r][c] = 2  
                    rottenq.append([r, c])
                    fresh -= 1
        minutes += 1
                            
    
    return minutes if fresh < 1 else -1
