from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l,r = 0,0
        n= len(s)
        maxLength = 1
        maxElefreq = 0

        while r < n:
            freq[s[r]]+=1
            maxElefreq = max(maxElefreq,freq[s[r]] )
            if ((r-l+1)-maxElefreq) <= k:
                maxLength = max(maxLength, r-l+1)
                r+=1
            else:
                freq[s[l]]-=1
                l+=1
                r+=1
        return maxLength
                


            
            
            
            


            



        