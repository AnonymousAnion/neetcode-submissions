# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head:

            return None

        left -= 1
        right -= 1
        
        current = head
        index = 0

        while current and index < left - 1:

            current = current.next
            index += 1

        # Record right before the reversing
        start = current if left > 0 else None

        def reverse(start_reverse, index, right) -> (ListNode, ListNode):

            prev = None
            current = start_reverse

            while current and index <= right:

                temp = current.next
                current.next = prev
                prev = current
                current = temp
                index += 1

            return start_reverse, prev, current

        if current and index < left:

            current = current.next
            index += 1

        # Reverse
        start_reverse, end_reverse, end = reverse(current, index, right)

        # Rewire connects around the reverse sublinked list
        if start: start.next = end_reverse
        if start_reverse: start_reverse.next = end

        # Return the head unless the head was included in reversals
        if start:

            return head

        else:

            # Return the end of the reversal section if the head was included
            # in reversals
            return end_reverse
