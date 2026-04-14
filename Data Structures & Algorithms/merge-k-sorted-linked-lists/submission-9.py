# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge_sorted(l1, l2) -> Optional[ListNode]:

            if not l1 and not l2:

                return None

            elif not l1:

                return l2

            elif not l2:

                return l1

            head = ListNode(-1)
            current = head

            while l1 and l2:

                if l1.val <= l2.val:

                    current.next = l1
                    l1 = l1.next

                else:

                    current.next = l2
                    l2 = l2.next

                current = current.next

            while l1:

                current.next = l1
                l1 = l1.next
                current = current.next

            while l2:

                current.next = l2
                l2 = l2.next
                current = current.next

            return head.next

        def divide(s: int, e: int) -> Optional[ListNode]:

            nonlocal lists

            if not lists:

                return None

            elif e - s <= 0:

                # print("e: ", e)
                # print("s: ", s)
                # print("Lists: ", lists)

                return lists[s]

            m = s + (e - s) // 2

            left = divide(s, m)
            right = divide(m + 1, e)
            combined = merge_sorted(left, right)

            return combined

        return divide(0, len(lists) - 1)