class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        total=sum(nums)
        for i in range(len(nums)):
            total=total-nums[i]
            if left==total:
                return i
                break
            left=left+nums[i]
        else:
            return -1