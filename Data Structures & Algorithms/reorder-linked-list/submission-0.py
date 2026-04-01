# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head

        # Find the halfway point
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            print(fast)

        # Reverse the second half

        second = slow.next
        prev = slow.next = None

        while second:

            temp = second.next
            second.next = prev
            prev = second
            second = temp

        current = head

        while prev:

            forward_temp = current.next
            reverse_temp = prev.next
            current.next = prev
            prev.next = forward_temp
            prev = reverse_temp
            current = forward_temp
