def isSymmetric(root):
    tree_left = []
    tree_right = []

    def getArr(arr, root, mode=False):
        if not root:
            arr.append(0)
            return 0
        arr.append(root.val)
        if mode:
            getArr(arr, root.left, mode)
            getArr(arr, root.right, mode)
        else:
            getArr(arr, root.right)
            getArr(arr, root.left)
        
    getArr(tree_left, root.left, True)
    getArr(tree_right, root.right)

    return tree_left == tree_right


# Neetcode
# def isSymmetric(root):

#     def dfs(left, right):
#         if not left and not right:
#             return True
        
#         if not left or not right:
#             return False
        
#         return (left.val == right.val and
#                 dfs(left.left, right.right) and
#                 dfs(left.right, right.left))
#     return dfs(root.left, root.right)


