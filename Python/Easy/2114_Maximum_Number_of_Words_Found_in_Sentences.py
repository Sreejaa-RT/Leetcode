class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxword=0
        for sentence in sentences:
            word=sentence.split()
            maxword=max(maxword,len(word))
        return maxword