# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:

            return None
        
        head = ListNode(-1)
        current = head
        min_node = True

        while min_node:

            min_node = None
            min_val = float("infinity")
            min_index = 0
            compressed_lists = []

            # Find the minimum node
            for i, cur in enumerate(lists):

                if cur:
                    
                    if cur.val < min_val:

                        min_val = cur.val
                        min_node = cur
                        min_index = i

            if min_node:

                current.next = min_node
                current = current.next
                lists[min_index] = min_node.next

        return head.next