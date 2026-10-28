class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split()
        if len(pattern)!=len(word):
            return False
        for i in range(len(pattern)):
            for j in range(i):
                if pattern[i]==pattern[j]:
                    if word[i]!=word[j]:
                        return False
                if pattern[i]!=pattern[j]:
                    if word[i]==word[j]:
                        return False
        return True
