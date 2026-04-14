class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return self.solve(root, p, q)

    def solve(self, root, p, q):
        if root is None:
            return None
        
        # If current node is p or q
        if root == p or root == q:
            return root
        
        left = self.solve(root.left, p, q)
        right = self.solve(root.right, p, q)
        
        # If both sides return non-null → this is LCA
        if left and right:
            return root
        
        # Otherwise return the non-null side
        return left if left else right
        