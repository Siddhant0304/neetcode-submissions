# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        l = []
        if not root: return ''
        q = deque()
        q.appendleft(root)
        l.append(str(root.val))
        while(q):
            temp = q.pop()
            if temp.left:
                q.appendleft(temp.left)
                l.append(str(temp.left.val))
            else:
                l.append('#')
            if temp.right:
                q.appendleft(temp.right)
                l.append(str(temp.right.val))
            else:
                l.append('#')
        print(l)
        return ','.join(l)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        data  = data.split(',')
        root  = TreeNode(data[0])
        q = deque()
        q.appendleft(root)
        i = 1
        while q:
            temp = q.pop()
            if data[i] != '#':
                leftNode = TreeNode(data[i])
                q.appendleft(leftNode)
                temp.left = leftNode
            if data[i+1] != '#': 
                rightNode = TreeNode(data[i+1])
                q.appendleft(rightNode)
                temp.right = rightNode
            i+=2
        return root
                
            


            
            



