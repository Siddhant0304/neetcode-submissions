class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''

        for i in range(len(s)):
            #odd length
            l,r= i,i 
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > len(res):
                    res = s[l:r+1]
                
                l-=1
                r+=1

            #even length
            l,r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1


        return res



            


        # code for longest palindromic subsequence
        # r = s[::-1]
        # n = len(s)
        # mat = [[0]*(n+1) for _ in range(n+1)]
        
        # for i in range(1,n+1):
        #     for j in range(1,n+1):
        #         if r[i-1] == s[j-1]:
        #             mat[i][j] = 1+ mat[i-1][j-1]
        #         else:
        #             mat[i][j] = max(mat[i-1][j], mat[i][j-1])
        
        # maxstr = ''
        # i = j = n
        # while i>0 and j>0:
        #     if s[i-1] == r[j-1]:
        #         maxstr += s[i-1]
        #         i-=1
        #         j-=1
        #     elif mat[i-1][j] >= mat[i][j-1]:
        #         i-=1
        #     else:
        #         j-=1
        # print(mat)
        # return maxstr

        

