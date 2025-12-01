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