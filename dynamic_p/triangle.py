


def minimumTotal(triangle):
    rows = 0
    cols = 0

    cache = {}
    def helper(row, col):
        if row > (len(triangle) - 1) or col > (len(triangle[col]) - 1):
            return float('inf')
        if (row, col) not in cache:
            cache[(row, col)] = triangle[row][col] + min(helper(row + 1, col), helper(row, col + 1))
        
        return cache[(row, col)]

    return helper(rows, cols)


# def minimumTotal(triangle):
#     result = 0
#     lastIndex = 0
#     for arr in triangle:
#         minNum = float('inf')
#         for idx in range(len(arr)):
#             if arr[idx] < minNum and (lastIndex == idx or lastIndex + 1 == idx):
#                 print(arr[idx], idx, minNum)
#                 lastIndex = idx
#                 minNum = arr[idx]
#         # print('lastIndex', idx)

#         # print('minNum', minNum) 

#         result += minNum
#     return result

            
# print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
# print(minimumTotal([[-10]]))
print(minimumTotal([[-1],[2,3],[1,-1,-3]])) # -1 ? 

