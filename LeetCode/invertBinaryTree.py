
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            pivot = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(pivot)
            return root

    def printTree(self,root):
        if(root != None):
            self._printTree(root)

    def _printTree(self,node):
        if(node != None):
            self._printTree(node.left)
            print(str(node.val) + ' ')
            self._printTree(node.right)


inputs = [4,2,7,1,3,6,9]
root = None
for node in inputs:
    root = TreeNode(root, node)

Solution.printTree(root)
