# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #two pointer

        dummy  = ListNode(0,head)
        slow  = dummy
        fast = head
        cntr = n
        while cntr > 0 and fast:
            fast = fast.next
            cntr-=1
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        tmp = slow.next
        slow.next = tmp.next
        tmp.next = None

        return dummy.next

        # cntr = 0
        # prev = None
        # length =  0
        
        # curr= head
        # while curr:
        #     curr = curr.next
        #     length +=1
        # if length-n == 0:
        #     return head.next

        # curr= head
        # n= length-n
        
        # for  _ in range(n-1):
        #     curr = curr.next
        # curr.next = curr.next.next
 
        # # this also works fine
        # # while curr and cntr <= n:
        # #     if cntr == n:
        # #         prev.next = curr.next
        # #         curr.next = None
        # #         curr = prev.next
        # #         cntr+=1

        # #     else:
        # #         prev = curr
        # #         curr = curr.next
        # #         cntr+=1
            
        # return head
        