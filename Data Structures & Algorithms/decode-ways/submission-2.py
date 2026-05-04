from collections import defaultdict
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = defaultdict(int)
        dp[n] = 1
        
        def dfs(i):
            if i in dp : return dp[i]
            if i > n:
                return 1
            if s[i] == "0": return 0

            res1 = dfs(i+1)

            res2 = 0
            if (i+1) < len(s) and (s[i] == "1" or (s[i]=='2' and s[i+1] in ("0123456"))):
                res2 += dfs(i+2)
            
            dp[i] = res1 + res2
            return dp[i]
        
        return dfs(0)



            
       

        