from typing import List
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        first=second=None
        for n in arr:
            if first is None or (n > first):
                second=first
                first=n
            elif n != first and (second is None or n > second):
                second=n
        return second if second is not None else -1

