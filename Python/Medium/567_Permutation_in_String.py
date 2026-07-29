class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s2)
        k=len(s1)
        found=False
        for i in range(n-k+1):
            sub=s2[i:i+k]
            if sorted(s1)==sorted(sub):
                found=True
                return True
        if not found:
            return False 