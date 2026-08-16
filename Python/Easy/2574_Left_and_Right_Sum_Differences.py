class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=[0]*len(nums)
        rightsum=[0]*len(nums)
        ans=[0]*len(nums)
        n=len(nums)
        for i in range(n):
            if i==0:
                leftsum[i]=0
            else:
                leftsum[i]=leftsum[i-1]+nums[i-1]
        for i in range(n-1,-1,-1):
            if i==n-1:
                rightsum[i]=0
            else:
                rightsum[i]=rightsum[i+1]+nums[i+1]
        for i in range(n):
            ans[i]=abs(leftsum[i]-rightsum[i])
        return ans