class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        line1=set("qwertyuiop")
        line2=set("asdfghjkl")
        line3=set("zxcvbnm")
        res=[]
        for word in words:
            w=set(word.lower())
            if w<=line1 or w<=line2 or w<=line3:
                res.append(word)
        return res