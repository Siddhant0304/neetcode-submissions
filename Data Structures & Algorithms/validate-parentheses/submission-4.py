from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        
        q = deque()
        pairs = {'}':'{',']':'[',')':'('}
        for c in s:
            if c in pairs.values():
                q.append(c)
            else:
                if not q or q[-1] != pairs[c]: return False
                q.pop()
        if len(q):return False
        return True