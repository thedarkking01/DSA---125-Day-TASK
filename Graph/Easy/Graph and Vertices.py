#link: https://www.geeksforgeeks.org/problems/graph-and-vertices/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=graph-and-vertices


class Solution:
    def count(self, n):
        # Code here
        return 2 ** (n * (n - 1) // 2)