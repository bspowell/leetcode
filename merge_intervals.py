# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
#  and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Algo:
# given an array of intervals
# - check if the last element of the first interval is greater than the first element of the second interval
# - if yes, merg first element of first interval with second element of second interval
# - if no, add first interval to result array
#  

def mergeIntervals(intervals):
    intervals.sort(key = lambda i: i[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        print('this is start: ', start, 'this is end: ', end)
        lastEnd = output[-1][1]
        
        if start <= lastEnd: 
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])
    
    return output



print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]])) #[[1,6],[8,10],[15,18]]
# print(mergeIntervals([[1,4],[4,5]])) # [[1,5]]
# print(mergeIntervals([[1,3],[2,6],[5,5],[1,18]])) # [[1, 18]]
# print(mergeIntervals([[1,4],[5,6]])) # [[1,4],[5,6]]
# print(mergeIntervals([[1,4],[0,4]])) # [[0,4]]
# print(mergeIntervals([[1,4],[0,1]])) # [[0,4]]


