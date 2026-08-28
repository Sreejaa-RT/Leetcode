class Solution:
    def isRectangleOverlap(self, rect1: List[int], rect2: List[int]) -> bool:
        if (rect1[0]==rect2[2] or rect1[1]==rect1[3] or \
            rect2[0]==rect2[2] or rect2[1]==rect2[3]):
            return False
        return not(
            rect1[2]<=rect2[0] or
            rect1[0]>=rect2[2] or
            rect1[1]>=rect2[3] or
            rect1[3]<=rect2[1]
        )