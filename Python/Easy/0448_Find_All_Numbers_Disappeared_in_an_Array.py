class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m=set(nums)
        res=[]
        for i in range(1,len(nums)+1):
            if i not in m:
                res.append(i)
        return res