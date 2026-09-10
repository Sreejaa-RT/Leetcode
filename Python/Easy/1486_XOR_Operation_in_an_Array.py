class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans=0
        for num in range(n):
            ans^=start+2*num
        return ans