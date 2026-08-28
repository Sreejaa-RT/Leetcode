class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        for i in range(len(matrix)):
            row_min=min(matrix[i])
            for j in range(len(matrix[0])):
                col_max=max(matrix[k][j] for k in range(len(matrix)))
                if matrix[i][j]==row_min and matrix[i][j]==col_max:
                    res.append(matrix[i][j])
        return res