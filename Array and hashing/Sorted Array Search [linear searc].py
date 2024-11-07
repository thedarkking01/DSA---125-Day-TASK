
class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        #Your code here
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == k:
                return True
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
                
        return False

