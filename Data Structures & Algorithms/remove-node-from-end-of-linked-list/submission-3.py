# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cntr = 0
        prev = None
        length =  0
        
        curr= head
        while curr:
            curr = curr.next
            length +=1
        if length-n == 0:
            return head.next

        curr= head
        n= length-n
        
        for  _ in range(n-1):
            curr = curr.next
        curr.next = curr.next.next
 

        # while curr and cntr <= n:
        #     if cntr == n:
        #         prev.next = curr.next
        #         curr.next = None
        #         curr = prev.next
        #         cntr+=1

        #     else:
        #         prev = curr
        #         curr = curr.next
        #         cntr+=1
            
        return head
        