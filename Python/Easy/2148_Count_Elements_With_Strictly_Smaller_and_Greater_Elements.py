class Solution:
    def countElements(self, nums: list[int]) -> int:
        m=min(nums)
        mx=max(nums)
        c=0
        for i in range(len(nums)):
            if nums[i]>m and nums[i]<mx:
                c+=1
        return c