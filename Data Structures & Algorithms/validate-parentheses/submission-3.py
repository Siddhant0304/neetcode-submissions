from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        
        q = deque()
        for i in range(len(s)):
            if s[i] in ('(','{','['):
                q.append(s[i])
            else:
                if not len(q): return False
                top = q.pop()
                if s[i] == ')' and top != '(': return False
                if s[i] =='}' and top !='{': return False
                if s[i] == ']' and top!='[': return False
        if len(q):return False
        return True