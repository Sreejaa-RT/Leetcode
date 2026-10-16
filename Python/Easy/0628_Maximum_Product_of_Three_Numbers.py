class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        p=nums[n-1]*nums[n-2]*nums[n-3]
        prd=nums[n-1]*nums[0]*nums[1]
        if p>prd:
            return p
        else:
            return prd