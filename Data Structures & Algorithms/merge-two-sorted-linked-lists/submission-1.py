# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2
        merged = None
        merged_head = None

        while curr1 or curr2:

            if curr1 and (not curr2 or curr1.val < curr2.val):

                lesser_node = curr1
                curr1 = curr1.next

            else:

                lesser_node = curr2
                curr2 = curr2.next

            if merged:

                merged.next = lesser_node
                merged = merged.next

            else:

                merged_head = merged = lesser_node

        return merged_head


