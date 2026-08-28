class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year,day,date=date.split("-")
        year=bin(int(year))[2:]
        day=bin(int(day))[2:]
        date=bin(int(date))[2:]
        return year+"-"+day+"-"+date