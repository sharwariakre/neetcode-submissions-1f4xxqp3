# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case: if input list is empty, return None
        if len(lists) == 0:
            return None
        
        # Keep merging pairs of lists until there's only one list left
        while len(lists) > 1:
            mergedLists = []

            # Merge lists in pairs
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # Handle odd number of lists by checking bounds
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                # Merge the two lists and add to the merged list array
                mergedLists.append(self.mergeTwoLists(l1, l2))
            
            # Update lists to merged result for next iteration
            lists = mergedLists
        
        # Only one fully merged list remains
        return lists[0]

    # Helper function to merge two sorted linked lists
    def mergeTwoLists(self, l1, l2):
        # Dummy node to simplify appending logic
        dummy = ListNode()
        tail = dummy

        # Merge nodes in sorted order
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # Append any remaining nodes
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next
