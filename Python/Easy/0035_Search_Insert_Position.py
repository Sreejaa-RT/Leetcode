class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        i=0
        j=n-1
        found=False
        while i<=j:
            if nums[i]==target:
                founnd=True
                return i
            if nums[i]<target:
                i+=1
            elif nums[i]>target:
                j-=1
        if not found:
            return j+1