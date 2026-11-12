class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude=0
        high=0
        for i in gain:
            altitude+=i
            high=max(high,altitude)
        return high