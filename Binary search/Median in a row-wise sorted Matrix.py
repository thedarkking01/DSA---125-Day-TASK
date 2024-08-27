# platform - Coding Ninjas 
# link = https://www.naukri.com/code360/problems/median-of-a-row-wise-sorted-matrix_1115473?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

def median(matrix: [[int]], m: int, n: int) -> int:
    def count_less_equal(x):
        # This function returns the count of elements less than or equal to x
        count = 0
        for row in matrix:
            # Using binary search to find the count of elements <= x in each row
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if row[mid] <= x:
                    l = mid + 1
                else:
                    r = mid
            count += l
        return count

    # Binary search on the value range of the matrix
    low, high = matrix[0][0], matrix[-1][-1]
    
    while low < high:
        mid = (low + high) // 2
        if count_less_equal(mid) < (m * n + 1) // 2:
            low = mid + 1
        else:
            high = mid

    return low