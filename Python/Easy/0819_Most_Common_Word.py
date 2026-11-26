import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        p=re.findall(r'[a-z]+',paragraph.lower())
        c=Counter(p)
        res=""
        for word in c:
            if word not in banned:
                if res=="" or c[word]>c[res]:
                    res=word

        return res