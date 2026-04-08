# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        current = head

        # Find the valid start of the linked list
        while current and current.val == val:

            current = current.next

        head = current
        
        while current:

            next_node = current.next

            while next_node and next_node.val == val:

                next_node = next_node.next

            current.next = next_node
            current = current.next

        return head