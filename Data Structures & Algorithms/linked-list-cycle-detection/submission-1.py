# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pntr1=pntr2=head
        while pntr2 and pntr2.next:
            pntr1 = pntr1.next
            pntr2 = pntr2.next.next
            if pntr1 == pntr2: return True
        return False

        
        