class Solution:
    def findComplement(self, num: int) -> int:
        bits=num.bit_length()
        n=num^(1<<bits)-1
        return n