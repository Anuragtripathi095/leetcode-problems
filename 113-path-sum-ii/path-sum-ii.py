# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, curr_sum, path):
            if not node:
                return
            
            # Add current node
            path.append(node.val)
            curr_sum += node.val

            # Check if it's a leaf and sum matches
            if not node.left and not node.right and curr_sum == targetSum:
                result.append(path[:])  # copy the path
            
            # Recurse
            dfs(node.left, curr_sum, path)
            dfs(node.right, curr_sum, path)

            # Backtrack
            path.pop()

        dfs(root, 0, [])
        return result