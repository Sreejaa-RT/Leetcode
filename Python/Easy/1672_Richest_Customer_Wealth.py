class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        for i in accounts:
            m=sum(i)
            maxi=max(maxi,m)
        return maxi