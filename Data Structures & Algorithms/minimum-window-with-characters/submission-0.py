from collections import defaultdict
class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        l,r, n = 0, 0, len(s)
        lookupt = defaultdict(int)
        windows = defaultdict(int)
        
        minLen = float('inf')
        res = ""
        
        for c in t:
            lookupt[c]+=1
        have, need = 0, len(lookupt)

        while r < n:
            c = s[r]
            windows[c]+=1
            if c in lookupt and windows[c] == lookupt[c]:
                    have+=1

            while have==need:
                if minLen > r-l+1:
                    minLen = r-l+1
                    res = s[l:r+1]
                windows[s[l]]-=1
                if s[l] in lookupt and windows[s[l]] < lookupt[s[l]]:
                    have-=1
                l+=1
                    
             
            r+=1

                     
        return res
