# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        return self.rinsert(root,val)
    def rinsert(self,root,val):
        if root is None:
            return TreeNode(val)
        elif val<root.val:
            root.left= self.rinsert(root.left,val)
        elif val>root.val:
            root.right= self.rinsert(root.right,val)
        return root
        