#Problem link : https://www.interviewbit.com/problems/painters-partition-problem/

class Solution:
    # @param A : integer (number of painters)
    # @param B : integer (time per unit length)
    # @param C : list of integers (lengths of boards)
    # @return an integer (minimum time modulo 10000003)
    
    def is_possible(self, C, A, mid, B):
        painters = 1  # start with one painter
        current_sum = 0  # track the amount of work for the current painter
        
        for length in C:
            current_sum += length  # add the board length to the current painter's workload
            
            # If the current painter's workload exceeds mid, assign a new painter
            if current_sum * B > mid:
                painters += 1
                current_sum = length  # the next painter starts with the current board
                
                # If the number of painters exceeds available painters, return False
                if painters > A:
                    return False
        
        return True  # it's possible to paint all boards with A painters and mid time
    
    def paint(self, A, B, C):
        MOD = 10000003  # as specified in the problem, answer must be modded by this value
        
        # Set the binary search bounds
        low, high = max(C) * B, sum(C) * B  # minimum and maximum possible time
        result = high  # initialize result with the highest possible time
        
        while low <= high:
            mid = (low + high) // 2  # mid point for binary search
            
            # Check if it's possible to paint all boards within 'mid' time
            if self.is_possible(C, A, mid, B):
                result = mid  # if possible, this is a candidate solution
                high = mid - 1  # try to find a smaller maximum time
            else:
                low = mid + 1  # if not possible, increase the time limit
        
        return result % MOD  
