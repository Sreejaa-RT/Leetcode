class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        s=set(nums)
        l=list(s)
        l.sort(reverse=True)
        if len(l)>=3:
            return l[2]
        else:
            return max(l)
        
