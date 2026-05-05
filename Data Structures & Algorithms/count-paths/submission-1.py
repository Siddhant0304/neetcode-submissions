class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[1][1] = 1
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1 and j==1: continue
                left = dp[i-1][j]
                right = dp[i][j-1]
                dp[i][j] = left+right
        return dp[m][n]


        # dp = [[-1]*n for _ in range(m)]

        # def f(i,j):
            
        #     if i==0 and j==0: return 1
        #     if i<0 or j<0: return 0
        #     if dp[i][j] != -1: return dp[i][j]

        #     left = f(i-1,j)
        #     right = f(i,j-1)
        #     dp[i][j] = left+ right
        #     return dp[i][j]
        
        # return f(m-1,n-1)
        