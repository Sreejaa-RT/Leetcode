.3class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res=[]
        c=0
        for i in range(1,n+1):
            if n%i==0:
                c+=1
            if c==k:
                return i
        else:
            return -1
        
        
        