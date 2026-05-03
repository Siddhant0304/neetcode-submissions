class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n =  len(board), len(board[0])
        visited = [[0]*n for _ in range(m)]


        def dfs(i,j,word):
            if word == "": return True
            if i<=-1 or j <=-1 or i>=m or j>=n or board[i][j]!= word[0] or visited[i][j]==1:
                return False
            
            visited[i][j]=1
            word = word[1:]
            left = dfs(i-1,j, word)
            right = dfs(i+1,j,word)
            up = dfs(i, j-1, word)
            down  = dfs(i,j+1,word)
            visited[i][j] = 0
            return right or down or up or left

        for i in range(m):
            for j in range(n):
                
                if (dfs(i,j,word) == True): return True

        return False


        
        
   

    
     
        