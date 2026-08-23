class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix=[[0]*n for _ in range(m)]
        for r,c in indices:
            for j in range(n):
                matrix[r][j]+=1
            for i in range(m):
                matrix[i][c]+=1
        c=0
        for row in matrix:
            for x in row:
                if x%2==1:
                    c+=1
        return c