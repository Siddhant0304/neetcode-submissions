class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n =  len(board), len(board[0])
        


        def dfs(i,j,word, visited):
            if word == "": return True
            if i<=-1 or j <=-1 or i>=m or j>=n or board[i][j]!= word[0] or visited[i][j]==1:
                return False
            
            visited[i][j]=1
            word = word[1:]
            left = dfs(i-1,j, word, visited)
            right = dfs(i+1,j,word,visited)
            up = dfs(i, j-1, word, visited)
            down  = dfs(i,j+1,word, visited)
            visited[i][j] = 0
            return right or down or up or left

        for i in range(m):
            for j in range(n):
                visited = [[0]*n for _ in range(m)]
                if (dfs(i,j,word, visited) == True): return True

        return False


        
        
   

    
     
        