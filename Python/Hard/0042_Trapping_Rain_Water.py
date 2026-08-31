class Solution:
    def trap(self, height: List[int]) -> int:
        left=right=water=0
        i=0
        j=len(height)-1
        while i<j:
            if height[i]<=height[j]:
                if height[i]>=left:
                    left=height[i]
                else:
                    water=water+left-height[i]
                i=i+1
            else:
                if height[j]>=right:
                    right=height[j]
                else:
                    water=water+right-height[j]
                j=j-1
        return water