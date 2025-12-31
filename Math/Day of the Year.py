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

# Constraints:
# date.length == 10
# date[4] == date[7] == '-', and all other date[i]‘s are digits
# date represents a calendar date between Jan 1, 1900 and Dec 31, 2019.

# Pseudocode:
# Define a function dayOfYear that takes a string date as input and returns an integer.
# Create an array arr containing the number of days in each month except February (assuming it's not a leap year).
# Split the input date string by "-" to extract the year, month, and day.
# Convert the extracted year, month, and day strings into integers.
# Initialize a variable totalDays to store the total number of days, initially set to the day of the month.
# Iterate over the months before the current month:
# Add the number of days in each month to the totalDays.
# Check if the month is greater than 2 and if the year is a leap year (divisible by 4) and either divisible by 400 or not divisible by 100:
# If true, increment totalDays by 1 to account for the leap day in February.
# Return the totalDays

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