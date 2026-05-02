import re
class Solution:
    def cleanStr(self,s):
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s) 
        l= cleaned.lower().split()
        newString = ''.join(l)
        return newString

    def isPalindrome(self, s: str) -> bool:

        st = self.cleanStr(s)
        i,j = 0, len(st)-1
        
        while i < j:
            if st[i] != st[j]: return False
            i+=1
            j-=1
        
        
        return True
        