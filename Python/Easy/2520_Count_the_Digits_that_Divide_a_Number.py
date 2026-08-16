class Solution:
    def countDigits(self, num: int) -> int:
        val=num
        c=0
        while num>0:
            d=num%10
            if val%d==0:
                c+=1
            num//=10
        return c