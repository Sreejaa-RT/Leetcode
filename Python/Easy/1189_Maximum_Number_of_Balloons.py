from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c=Counter(text)
        b=c['b']
        a=c['a']
        l=c['l']//2
        o=c['o']//2
        n=c['n']
        return min(b,a,l,o,n)
        