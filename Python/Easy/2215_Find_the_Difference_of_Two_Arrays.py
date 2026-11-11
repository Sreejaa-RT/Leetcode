class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1=set(nums1)
        s2=set(nums2)
        res1=list(s1-s2)
        res2=list(s2-s1)
        return [res1,res2]