class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        far=0
        curr=0
        jump=0
        for i in range(n-1):
            if i+nums[i]>far:
                far=i+nums[i]
            if i==curr:
                jump+=1
                curr=far
        return jump
