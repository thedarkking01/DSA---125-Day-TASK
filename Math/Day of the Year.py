# leetcode 1154. Day of the Year
# Difficulty: Easy  
# url : https://leetcode.com/problems/day-of-the-year/

# Problem Statement :

# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.


# Examples:
 

# Example 1:

# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.

# Example 2:

# Input: date = "2019-02-10"
# Output: 41.

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