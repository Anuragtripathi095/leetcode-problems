class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        # If left is null, go right
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # If right is null, go left
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # If both exist
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))