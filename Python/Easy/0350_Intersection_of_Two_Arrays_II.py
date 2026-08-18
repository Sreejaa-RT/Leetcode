from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1=Counter(nums1) 
        c2=Counter(nums2)
        ans=[]
        for x in c1:
            if x in c2:
                ans+=[x]*min(c1[x],c2[x])
        return ans