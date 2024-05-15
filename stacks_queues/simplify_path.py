# It must start with a single slash '/'.
# Directories within the path should be separated by only one slash '/'.
# It should not end with a slash '/', unless it's the root directory.
# It should exclude any single or double periods used to denote current or parent directories.
# ... is a valid name for a directory
# 


# start from right
# separate sting into array based on slashes
# iterate from end to start 
# if it's .., then remove next one in array (-1)
#   e.g "/home/user/Documents/../Pictures" => "/home/user/Pictures"
# if it's a dot, remove dot
# 
# rejoin string with slashes afterward

def simplifyPath(path):
    arr = path.split('/')
    stack = []

    for el in arr:
        if el == '..' and stack:
            stack.pop()
            continue
        
        if el not in ['', '.', '..']:
            stack.append(el)
    
    return '/' + '/'.join(stack)

    #     print(stack)
    #     if arr[i] == '.' or arr[i] == '':
    #         continue
    #     elif arr[i] == '..' and len(stack) > 1:
    #         stack.pop(-1)
    #     elif arr[i] != '..' and arr[i] != '.':
    #         stack.append(arr[i])
    
    # if len(stack) < 2:
    #     return '/'
    # else:
    #     return '/' + '/'.join(stack)

# use a stack to create a new array 


print(simplifyPath("/home/user/Documents/../Pictures"))
print(simplifyPath("/.../a/../b/c/../d/./"))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/../"))
print(simplifyPath("/home/"))
print(simplifyPath("/../"))



#Tony's answer
# def simplifyPath(path):
#     stack = collections.deque()
    
#     for item in path.split('/'):
#         if item == '..' and stack:
#             stack.pop()
#             continue
        
#         if item not in ['', '.', '..']:
#             stack.append(item)
    
#     return '/' + '/'.join(stack)