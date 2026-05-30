class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkColumn():
            for i in range(9):
                hashset = set()
                for j in range(9):
                    if board[j][i]=='.': continue
                    if board[j][i] in hashset:
                        return False
                    else:
                        hashset.add(board[j][i])
            return True

        def checkRow():
            for i in range(9):
                hashset = set()
                for j in range(9):
                    if board[i][j]=='.': continue
                    if board[i][j] in hashset:
                        return False
                    else:
                        hashset.add(board[i][j])
            return True
        
        def checkSubMatrix(m,n):
            hashset = set()
            for i in range(m,m+3):
                for j in range(n,n+3):
                    if board[i][j]=='.': continue
                    if board[i][j] in hashset:
                        return False
                    else:
                        hashset.add(board[i][j]) 
            return True
        
        if not checkColumn(): return False
        if not checkRow(): return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                if not checkSubMatrix(i,j): return False
        
        return True

            
        