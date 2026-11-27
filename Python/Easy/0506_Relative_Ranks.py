class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        d={}
        sortedscore=sorted(score,reverse=True)
        for i in range(len(sortedscore)):
            if i==0:
                d[sortedscore[i]]="Gold Medal"
            elif i==1:
                d[sortedscore[i]]="Silver Medal"
            elif i==2:
                d[sortedscore[i]]="Bronze Medal"
            else:
                d[sortedscore[i]]=str(i+1)
        return [d[x] for x in score]