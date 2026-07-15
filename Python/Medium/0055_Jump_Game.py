class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far=0
        for i in range(len(nums)):
            if i>far:
                far=i
                return False
                break
            if i+nums[i]>far:
                far=i+nums[i]
        else:
           return True