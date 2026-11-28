class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words=title.split()
        res=[]
        for word in words:
            if len(word)<3:
                w=word.lower()
            else:
                w=word.capitalize()
            res.append(w)
        return " ".join(res)