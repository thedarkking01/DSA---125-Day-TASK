class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xaxis = coordinates[1][0] - coordinates[0][0]
        yaxis = coordinates[1][1] - coordinates[0][1]

        for i in range(1, len(coordinates) - 1):
            x = coordinates[i+1][0] - coordinates[i][0]
            y = coordinates[i+1][1] - coordinates[i][1]

            if x * yaxis != y * xaxis:
                return False

        return True
