def countNodes(self, root) -> int:
    if root is None: 
        return 0
    elif (root.left is None and root.right is None): 
        return 1 
    else: 
        return 1+self.countNodes(root.left) + self.countNodes(root.right) 