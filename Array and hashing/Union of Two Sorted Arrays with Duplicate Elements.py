from typing import List

class Solution:
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a: List[int], b: List[int]) -> List[int]:
        i, j = 0, 0
        result = []
        
        while i < len(a) and j < len(b):
            # Skip duplicates in array `a`
            while i > 0 and i < len(a) and a[i] == a[i - 1]:
                i += 1
            # Skip duplicates in array `b`
            while j > 0 and j < len(b) and b[j] == b[j - 1]:
                j += 1
            
            if i < len(a) and j < len(b):
                if a[i] < b[j]:
                    result.append(a[i])
                    i += 1
                elif a[i] > b[j]:
                    result.append(b[j])
                    j += 1
                else:  # a[i] == b[j]
                    result.append(a[i])
                    i += 1
                    j += 1

        # Add remaining elements from array `a`
        while i < len(a):
            if i == 0 or a[i] != a[i - 1]:  # avoid duplicates
                result.append(a[i])
            i += 1

        # Add remaining elements from array `b`
        while j < len(b):
            if j == 0 or b[j] != b[j - 1]:  # avoid duplicates
                result.append(b[j])
            j += 1

        return result