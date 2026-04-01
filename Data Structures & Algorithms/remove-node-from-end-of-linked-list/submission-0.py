# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        current = head
        length = 0 
        while current:

            current = current.next
            length += 1

        target_index = length - n - 1

        if target_index < 0:

            current = head.next
            head.next = None
            head = current
            return head

        current = head
        index = 0

        while current and index < target_index:

            current = current.next
            index += 1

        current.next = current.next.next

        return head