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
        min_heap = []

        # Initialize the minheap
        for i, cur in enumerate(lists):

            if cur:
                
                heapq.heappush(min_heap, (cur.val, (i, cur)))

        while min_heap:

            min_val, node = heapq.heappop(min_heap)
            min_index = node[0]
            min_node = node[1]

            if min_node:

                current.next = min_node
                current = current.next
                lists[min_index] = min_node.next

                if lists[min_index]:

                    heapq.heappush(min_heap, (lists[min_index].val, (min_index, lists[min_index])))

        return head.next