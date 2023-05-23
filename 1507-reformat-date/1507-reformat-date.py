class Solution:
    def reformatDate(self, date: str) -> str:
        month2num = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 
                     'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        
        date = date.split(' ')
        day = "".join([char for char in date[0] if char.isnumeric()])
        return date[2] + '-' + month2num[date[1]] + '-' + (day if len(day) == 2 else ('0' + day))