class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head:
            return None
        
        # Base case: single node
        if not head.next:
            return TreeNode(head.val)
        
        # Find middle using slow-fast pointer
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Disconnect left half
        prev.next = None
        
        # slow is middle → root
        root = TreeNode(slow.val)
        
        # Recursively build left and right
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        
        return root