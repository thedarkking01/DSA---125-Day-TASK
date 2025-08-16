class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        max_len = 0
        while l < n - 2:  # Need at least 3 elements to form a mountain
            # Check for start of increasing sequence
            if arr[l] < arr[l + 1]:
                r = l + 1
                # climb up
                while r < n - 1 and arr[r] < arr[r + 1]:
                    r += 1
                # Check for peak and start of descent
                if r < n - 1 and arr[r] > arr[r + 1]:
                    # climb down
                    while r < n - 1 and arr[r] > arr[r + 1]:
                        r += 1
                    max_len = max(max_len, r - l + 1)
                else:
                    r += 1  # no descent, move on
                l = r  # move left pointer to right pointer for next check
            else:
                l += 1  # skip flat or decreasing regions
        return max_len