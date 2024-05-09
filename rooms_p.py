
# Time Complexity: O(n log n) due to sorting the start and end time lists (st and et).
# Space Complexity: O(n) due to the additional space used by the st and et lists.


def rooms(arr):
    st = [n[0] for n in arr]
    et = [n[1] for n in arr]
    st.sort()
    et.sort()
    l = 0
    r = 0
    rooms = 0
    while l < len(st):
        if st[l] < et[r]:
            rooms += 1
        else:
            r += 1
        l += 1
    return rooms

# def rooms(intervals):
#     takes all the inner arrays, then zip creates two arrays with same indexes [0,5,15]
#     and then sorts it with map
#     ends, starts = map(sorted, (zip(*intervals)))   
#     e = 0
#     count = 0

#     for s in range(len(starts)):
#         if starts[s] < ends[e]:
#             count += 1
#         else:
#             e += 1

#     return count


print(rooms([[0, 30], [5, 10], [15, 20]]) == 2)                   
print(rooms([[7, 10], [2, 4]]) == 1)                               
print(rooms([[1, 2], [3, 4], [5, 6]]) == 1)                         
print(rooms([[1, 4], [2, 5], [3, 6]]) == 3)               
print(rooms([[1, 3], [3, 6], [6, 8]]) == 1)                          
print(rooms([[1, 10]]) == 1)                                        
print(rooms([[1, 3], [2, 4], [4, 6]]) == 2)                          
print(rooms([[1, 5], [2, 3], [4, 6], [5, 7]]) == 2)                
print(rooms([[0, 5], [1, 3], [2, 6], [4, 7], [5, 9], [8, 10]]) == 3) 
print(rooms([[1, 2], [2, 3], [3, 4], [4, 5]]) == 1)            
print(rooms([[1, 20], [5, 10], [11, 15], [16, 18]]) == 2)         
print(rooms([[1, 4], [1, 3], [1, 2], [1, 5]]) == 4) 