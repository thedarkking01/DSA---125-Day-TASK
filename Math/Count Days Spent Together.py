
# Problem Statement :
    # Alice and Bob are traveling to Rome for separate business meetings.
    # You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.
    # Return the total number of days that Alice and Bob are in Rome together.
    # You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].


# Examples:

#  Example 1:
    # Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
    # Output: 3
    # Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.

# Example 2:
    # Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
    # Output: 0
    # Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.



# Constraints:
    # All dates are provided in the format "MM-DD".
    # Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
    # The given dates are valid dates of a non-leap year

# Pseudocode:
    # Define a class Solution.
    # Initialize an array daysOfMonth containing the number of days in each month.
    # Define a function countDaysTogether that takes four strings arriveAlice, leaveAlice, arriveBob, and leaveBob as input and returns an integer.
    # Call the function getDays to convert the arrival and departure dates of both Alice and Bob into the number of days since the beginning of the year.
    # If either Alice's departure date is before Bob's arrival date or Bob's departure date is before Alice's arrival date, return 0 as they don't overlap.
    # Calculate the overlap of their stay by finding the maximum of the arrival dates and the minimum of the departure dates. Add 1 to account for inclusive counting.
    # Return the absolute difference between the maximum and minimum dates plus 1.
    # Define a private function getDays that takes a string str  as input and returns an integer representing the number of days since the beginning of the year.
    # Extract the month and day from the input string str.
    # Iterate over each month before the current month and accumulate the total number of days.
    # Add the number of days in the current month to the total.
    # Return the total number of days.
class Solution:
    daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def getDays(self, s: str) -> int:
        total = 0
        month = int(s[:2])
        days = int(s[3:])
        for i in range(month - 1):
            total += self.daysOfMonth[i]
        total += days
        return total
    
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        x1 = self.getDays(arriveAlice)
        y1 = self.getDays(leaveAlice)
        x2 = self.getDays(arriveBob)
        y2 = self.getDays(leaveBob)
        if y1 < x2 or y2 < x1:
            return 0
        return abs(max(x1, x2) - min(y1, y2)) + 1