# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return 
        
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
         
        i, j = 0, len(arr)-1
        
        node = None
        while i<=j:
            if i==j:
                if node: node.next = arr[i]
                node = arr[i]
            
            else:
                if node: node.next=arr[i]
                arr[i].next = arr[j]
                node = arr[j]
              
            i+=1
            j-=1
       
        if node:
            node.next = None