class TreeNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    
    def children(self):
        return (self.left,self.right)
    
    def __str__(self):
        return "Left = ({}), Right =  ({})".format(self.left, self.right)