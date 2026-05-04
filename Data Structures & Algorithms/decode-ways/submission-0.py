class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        def f(i):
            if i   in dp: return dp[i]
            if i == len(s) : return 1
            if i > len(s): return 0
            if s[i] == "0": 
                return 0
            res1 = f(i+1)
            res2 = 0
            if (i+1 < len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456"))):
                res2 = f(i+2)
            dp[i] = res1 + res2
            return  dp[i]
        return f(0)

        