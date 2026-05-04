class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        n = len(s)
        cnt = 0
        for i in range(n):
            #odd length
            l,r = i,i
            while l>-1 and r<n and s[l]==s[r]:
                cnt+=1
                l-=1
                r+=1

            l,r = i, i+1
            while l>-1 and r<n and s[l]==s[r]:
                cnt+=1
                l-=1
                r+=1

        return cnt



        