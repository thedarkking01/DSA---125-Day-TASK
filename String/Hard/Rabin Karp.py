# Approach
# Compute the number of times a needs to be repeated to have a string with length at least as long as b.
# Check if b is a substring of the repeated a string of length n. If yes, return n.
# If b is not a substring of a repeated n times, check if it is a substring of a repeated n+1 times. If yes, return n+1.
# If b is not a substring of either a repeated n times or a repeated n+1 times, return -1.


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = divmod(len(b), len(a))
        if m:
            n += 1
        if b in a * n:
            return n
        elif b in a * (n+1):
            return n+1
        else:
            return -1