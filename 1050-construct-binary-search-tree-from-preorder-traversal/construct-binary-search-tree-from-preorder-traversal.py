class Solution(object):
    def bstFromPreorder(self, preorder):
        inorder = sorted(preorder)
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        self.pre_idx = 0
        
        def build(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            root = TreeNode(root_val)
            
            mid = inorder_map[root_val]
            
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(preorder) - 1)