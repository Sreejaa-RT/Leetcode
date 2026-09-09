class Solution:
    def totalNQueens(self, n: int) -> int:
        col=[False]*n
        da1=[False]*(2*n)
        da2=[False]*(2*n)
        c=0
        def find(row):
            nonlocal c
            if row==n:
                c+=1
                return 
            for i in range(n):
                d1=row-i+n
                d2=row+i
                if not col[i] and not da1[d1] and not da2[d2]:
                    col[i]=True
                    da1[d1]=True
                    da2[d2]=True
                    find(row+1)
                    col[i]=False
                    da1[d1]=False
                    da2[d2]=False
        find(0)
        return c