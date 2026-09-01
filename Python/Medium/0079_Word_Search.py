class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r=len(board)
        c=len(board[0])
        sol=[[0]*c for _ in range(r)]
        def find(i,j,k):
            if i<0 or j<0 or i>=r or j>=c:
                return False
            if sol[i][j]==1:
                return False
            if board[i][j]!=word[k]:
                return False
            if k==len(word)-1:
                return True
            sol[i][j]=1
            if find(i-1,j,k+1):
                return True
            if find(i,j-1,k+1):
                return True
            if find(i+1,j,k+1):
                return True
            if find(i,j+1,k+1):
                return True
            sol[i][j]=0
            return False
        for i in range(r):
            for j in range(c):
                if find(i,j,0):
                    return True
        return False
            