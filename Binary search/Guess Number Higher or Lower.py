# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r=1,n
        while l<=r:
            m=(l+r)//2
            myguess=guess(m)
            if myguess == 0:
                return m
            elif myguess== -1:
                r=m-1
            else:
                l=m+1


in Java 

// The guess API is defined for you.
// int guess(int num);

public class Solution {
    public int guessNumber(int n) {
        int left = 1, right = n;

        while (left <= right) {
            int mid = left + (right - left) / 2; // Avoids potential overflow
            int res = guess(mid);
            
            if (res == 0) {
                return mid;
            } else if (res < 0) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return -1; // This should never be reached if the number is guaranteed to exist
    }
}

            