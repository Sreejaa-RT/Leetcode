class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def find(data):
            rem=0
            for n in data:
                if rem==0:
                    if n>>7==0:
                        rem=0
                    elif n>>5==0b110:
                        rem=1
                    elif n>>4==0b1110:
                        rem=2
                    elif n>>3==0b11110:
                        rem=3
                else:
                    return False
            else:
                if n>>6!=0b10:
                    return False
                rem-=1
            return rem==0
        ans=find(data)
        return ans   