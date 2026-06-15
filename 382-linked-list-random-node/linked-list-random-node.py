import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result = self.head.val
        curr = self.head.next
        i = 2

        while curr:
            if random.randint(1, i) == 1:
                result = curr.val

            curr = curr.next
            i += 1

        return result