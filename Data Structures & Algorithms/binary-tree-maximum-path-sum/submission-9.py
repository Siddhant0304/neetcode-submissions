# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_ans = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            # Recursively find the max sum for left and right subtrees. 
            # Ignore subtrees that return a negative sum (treat as 0).
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            # Update the global maximum by considering the current node as the "highest point" 
            # of a potential path (splitting left and right).
            current_path_sum = left + right + node.val
            self.max_ans = max(self.max_ans, current_path_sum)
            
            # Return the maximum gain this node can contribute to its parent. 
            # It must only choose ONE branch (left or right) to maintain a valid path.
            return node.val + max(left, right)

        dfs(root)
        return self.max_ans
        # maxAns = float('-inf')

        # def dfs(node):
        #     nonlocal maxAns
        #     if not node: return 0
        #     left = dfs(node.left)
        #     right = dfs(node.right)
          
        #     current = node.val
        #     if left > 0:
        #         current+= left
        #     else:left =0
        #     if right > 0:
        #         current+=  right
        #     else:right =0
            
        #     maxAns = max(maxAns,current)
          
        #     return node.val + max(left, right)
        # dfs(root)
        
        # return maxAns

       
        

    
            

        

