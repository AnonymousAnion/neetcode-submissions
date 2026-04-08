# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head:

            return True
        
        # Identify the midpoint with fast and slow pointers
        prev_slow = None
        slow = head
        fast = head

        while fast and fast.next:

            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        # Reverse the Second Half
        if prev_slow:

            prev_slow.next = None

        current = slow.next

        while slow:

            slow.next = prev_slow
            prev_slow = slow
            slow = current
            current = current.next if current else None

        right = prev_slow
        left = head

        while left and right:

            print("left: ", left.val)
            print("right: ", right.val)

            if left.val != right.val:

                return False

            left = left.next
            right = right.next

        return True