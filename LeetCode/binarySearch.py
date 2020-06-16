class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

class Solution:
    def searchBST(self, root, val):
        sln=[]
        while root != None:
            if root.data == val:
                return root   
            else:
                if root.data > val and root.left != None:
                    root = root.left
                elif root.data < val and root.right != None:
                    root = root.right
                else: 
                    return None
        if root.data == None:
            return None
        else:
            while root != None:
                sln.append(root.data)
                if root.left != None:
                    root = root.left
                elif root.right != None:
                    root = root.right
            return(sln)

# Use the insert method to add nodes
root = Node(4)
root.insert(2)
root.insert(7)
root.insert(3)
root.insert(1)

root.PrintTree()

sln = Solution()
print(sln.searchBST(root, 2))