#platform = Interview bit
class Solution:
    # @param A : list of integers (number of pages in each book)
    # @param B : integer (number of students)
    # @return an integer (minimum possible maximum number of pages)

    def isPossible(self, A, n, B, curr_min):
        students_required = 1
        curr_sum = 0
        
        for i in range(n):
            if A[i] > curr_min:
                return False
            
            if curr_sum + A[i] > curr_min:
                students_required += 1
                curr_sum = A[i]
                
                if students_required > B:
                    return False
            else:
                curr_sum += A[i]
        
        return True

    def books(self, A, B):
        n = len(A)
        if n < B:
            return -1
        
        total_sum = sum(A)
        max_book = max(A)
        
        low, high = max_book, total_sum
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.isPossible(A, n, B, mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result
