class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum=0
        temp=x
        while temp>0:
            d=temp%10
            sum+=d
            temp//=10
        if x%sum==0:
            return sum
        else:
            return -1