# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        # Map value -> index for quick lookup in inorder
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        self.pre_idx = 0
        
        def helper(left, right):
            if left > right:
                return None
            
            # Pick current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            root = TreeNode(root_val)
            
            # Split inorder into left and right subtree
            mid = inorder_map[root_val]
            
            # Build left subtree
            root.left = helper(left, mid - 1)
            # Build right subtree
            root.right = helper(mid + 1, right)
            
            return root
        
        return helper(0, len(inorder) - 1)