from typing import List, Optional

# LeetCode already provides this class
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.build(1, n)
    
    def build(self, start: int, end: int) -> List[Optional[TreeNode]]:
        if start > end:
            return [None]
        
        all_trees = []
        
        for root_val in range(start, end + 1):
            left_subtrees = self.build(start, root_val - 1)
            right_subtrees = self.build(root_val + 1, end)
            
            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(root_val)
                    root.left = left
                    root.right = right
                    all_trees.append(root)
        
        return all_trees