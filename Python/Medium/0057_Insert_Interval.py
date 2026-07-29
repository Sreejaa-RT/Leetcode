class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res=[]
        for i in intervals:
            if not res:
                res.append(i)
            else:
                if i[0]<=res[-1][1]:
                    res[-1][1]=max(res[-1][1],i[1])
                else:
                    res.append(i)
        return res
