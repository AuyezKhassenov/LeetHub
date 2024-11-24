class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        month_to_num = {"Jan": "1", 
                        "Feb": "2", 
                        "Mar": "3", 
                        "Apr": "4", 
                        "May": "5", 
                        "Jun": "6", 
                        "Jul": "7", 
                        "Aug": "8", 
                        "Sep": "9", 
                        "Oct": "10", 
                        "Nov": "11", 
                        "Dec": "12"}
        month = month_to_num[month]
        day = "".join(char for char in day if char.isnumeric())
        month = "0" * (2-len(month)) + month
        day = "0" * (2-len(day)) + day
        return f"{year}-{month}-{day}"