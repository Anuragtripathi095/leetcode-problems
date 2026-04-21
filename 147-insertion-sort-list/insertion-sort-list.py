# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)   # Dummy node for sorted list
        curr = head
        
        while curr:
            prev = dummy
            
            # Find correct position to insert current node
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            next_node = curr.next   # Save next node
            
            # Insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr
            
            curr = next_node
        
        return dummy.next