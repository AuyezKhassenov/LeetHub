class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        month_to_num = {"Jan": "01", 
                        "Feb": "02", 
                        "Mar": "03", 
                        "Apr": "04", 
                        "May": "05", 
                        "Jun": "06", 
                        "Jul": "07", 
                        "Aug": "08", 
                        "Sep": "09", 
                        "Oct": "10", 
                        "Nov": "11", 
                        "Dec": "12"}
        month = month_to_num[month]
        day = "".join(char for char in day if char.isnumeric())
        day = "0" * (2-len(day)) + day
        return f"{year}-{month}-{day}"