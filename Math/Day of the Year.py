class Solution:
    def dayOfYear(self, date: str) -> int:
        arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        monthD = date.split("-")
        year = int(monthD[0])
        month = int(monthD[1])
        days = int(monthD[2])
        totalDays = days
        for i in range(month - 1):
            totalDays += arr[i]
        if month > 2 and year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
            totalDays += 1
        return totalDays