class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        t=0
        for start in range(len(arr)):
            for end in range(start,len(arr)):
                length=end-start+1
                if length%2==1:
                    t+=sum(arr[start:end+1])
        return t