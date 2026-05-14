class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '': return 0
        l,r =0,1
        unique_set = set(s[l])
        n = len(s)
        max_len = 1

        while r<n:
            if s[r] not in unique_set:
                unique_set.add(s[r])      
                max_len = max(max_len, len(unique_set))
                r+=1
                
            else:
                unique_set.remove(s[l])
                l+=1
        
        max_len = max(max_len,len(unique_set))
        return max_len

        # if len(s)==0: return 0
        # unique = set()
        # n = len(s)
        # l,r = 0,1
        # maxLen = 1
        # unique.add(s[l])
        
        # while r < n:
        #     if s[r] in unique: 
        #         unique.remove(s[l])
        #         l+=1

        #     else:
        #         maxLen = max(maxLen,len(s[l:r+1]))
        #         unique.add(s[r])
        #         r+=1

        # return maxLen

        