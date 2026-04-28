# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    k_ele = None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(node):
            if not node: return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.k_ele = node.val
                return
            
            inorder(node.right)
            
        inorder(root)
        return self.k_ele