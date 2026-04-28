# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < q.val: 
            min_n, max_n = p.val,q.val
        else: min_n, max_n = q.val,p.val
        
        while(root):
            if min_n == root.val or max_n == root.val: 
                return root
            if min_n < root.val and max_n > root.val : 
                return root
            
            if min_n < root.val and max_n < root.val:
                root = root.left
            else:
                root = root.right
            







        