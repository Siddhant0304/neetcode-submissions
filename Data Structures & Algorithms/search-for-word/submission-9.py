class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n =  len(board), len(board[0])
        path = set()

        def dfs(i,j,word):
            if word == "": return True
            if i<=-1 or j <=-1 or i>=m or j>=n or board[i][j]!= word[0] or (i,j) in path:
                return False
            path.add((i,j))
            word = word[1:]
            res = (dfs(i-1,j, word) or 
                   dfs(i+1,j, word) or 
                   dfs(i,j-1, word) or 
                   dfs(i,j+1,word))
            
            path.remove((i,j))
            return res

        for i in range(m):
            for j in range(n): 
                if (dfs(i,j,word) == True): return True

        return False


        
        
   

    
     
        