from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        ans=0
        odd=False
        for x in count:
            if count[x]%2==0:
                ans+=count[x]
            else:
                ans+=count[x]-1
                odd=True
        if odd:
            ans+=1
        return ans