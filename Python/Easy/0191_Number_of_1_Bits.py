class Solution:
    def hammingWeight(self, n: int) -> int:
       b=bin(n)
       count=b.count('1')
       return count 