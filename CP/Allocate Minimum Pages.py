class Solution:
    
    #Function to find minimum number of pages.
    def isPossible(self, arr, n, m, max_pages):
        student_count = 1
        current_pages = 0
        
        for pages in arr:
            if current_pages + pages > max_pages:
                student_count += 1
                current_pages = pages
                
                if student_count > m:
                    return False
            else:
                current_pages += pages
        
        return True
    
    # Function to find the minimum possible maximum pages allocation
    def findPages(self, n, arr, m):
        if m > n:  # More students than books
            return -1
        
        low = max(arr)
        high = sum(arr)
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.isPossible(arr, n, m, mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return result