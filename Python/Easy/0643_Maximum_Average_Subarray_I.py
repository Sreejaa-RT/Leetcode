class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr=sum(nums[:k])
        maxi=curr
        for i in range(k,len(nums)):
            curr=curr-nums[i-k]+nums[i]
            maxi=max(maxi,curr)
        return maxi/k