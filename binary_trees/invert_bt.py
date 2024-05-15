
def invertTree(self, node):
    if not node:
        return
    
    tmp = node.left
    node.left = node.right
    node.right = tmp

    self.invertTree(node.left)
    self.invertTree(node.right)
    
    return node

