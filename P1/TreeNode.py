## Class for node of binary tree (can be improved )
class TreeNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    
    def children(self):
        return (self.left,self.right)
    