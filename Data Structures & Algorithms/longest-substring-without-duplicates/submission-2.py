class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        unique = set()
        n = len(s)
        l,r = 0,1
        maxLen = 1
        unique.add(s[l])
        
        while r < n:
            if s[r] in unique: 
                unique.remove(s[l])
                l+=1

            else:
                maxLen = max(maxLen,len(s[l:r+1]))
                unique.add(s[r])
                r+=1

        return maxLen

        