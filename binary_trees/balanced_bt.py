def isBalanced(root):

    def dfs(root):
        if not root:
            return [True, 0]
        
        left, right = dfs(root.left), dfs(root.right)
        balanced = (left[0] and right[0] 
                    and abs(left[1] - right[1]) <= 1)

        return [balanced, 1 + max(left[1], right[1])]
    
    return dfs(root)[0]


#garret
# class Solution:
#     def isBalanced(self, root):
#         if root is None:
#             return True

#         def maxDepth(node):
#             if node == None:
#                 return 0

#             return 1 + max(maxDepth(node.left), maxDepth(node.right))

#         def checkDepth(node):
#             if node == None:
#                 return 0

#             # print(maxDepth(node), maxDepth(node.left), maxDepth(node.right))
#             return abs(maxDepth(node.left) - maxDepth(node.right)) <= 1

#         def helper(node):
#             if node == None:
#                 return True
#             if checkDepth(node) is False:
#                 return False
#             return helper(node.left) and helper(node.right)

#         return helper(root)
