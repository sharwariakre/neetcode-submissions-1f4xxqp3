# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, start, end):
        stop = end.next  # capture once before any modifications
        prev = stop
        curr = start
        while curr != stop:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        prev_tail = dummy
        curr = head
        start = head
        while curr:
            for i in range(k - 1):
                curr = curr.next
                if curr is None:
                    return dummy.next

            next_start = curr.next
            self.reverseList(start, curr)   # start.next already set to next_start inside
            prev_tail.next = curr
            prev_tail = start
            start = next_start
            curr = start
        return dummy.next


            
            
