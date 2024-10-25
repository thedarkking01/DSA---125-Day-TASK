#User function Template for python3

class Solution:
	def NthRoot(self, n, m):
		# Code here
		if n == 1:
            return m  # The 1st root of m is m itself.
        if m == 1:
            return 1  # Any root of 1 is 1.
		l,r=0,m
		while l<=r:
		    mid=(l+r)//2
		    mid_squared = mid **n
		    if mid_squared==m:
		        return mid
		    elif mid_squared < m:
                l = mid + 1  # Search in the higher half
            else:
                r = mid - 1  # Search in the lower half

        return -1  # No integer root found

