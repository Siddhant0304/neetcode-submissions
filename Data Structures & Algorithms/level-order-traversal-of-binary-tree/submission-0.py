# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        ans = []
        if not root: return ans
        q.appendleft(root)

        while(q):
            level = []
            for i in range(len(q)):
                curr = q.pop()
                level.append(curr.val)
                if curr.left:
                    q.appendleft(curr.left)
                if curr.right:
                    q.appendleft(curr.right)
                
            ans.append(level)

        return ans


        
        