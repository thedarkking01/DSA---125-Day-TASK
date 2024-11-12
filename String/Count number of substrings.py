#User function Template for python3

class Solution:
    def substrCount (self,s, k):
        # your code here
        def atMostKDistinct(k):
            count=0
            left=0
            freq={}
            distinct = 0
            for right in range(len(s)):
                if s[right] not in freq or freq[s[right]] == 0:
                    distinct += 1
                freq[s[right]] = freq.get(s[right], 0) + 1
                
                # If the window has more than k distinct characters, shrink it
                while distinct > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        distinct -= 1
                    left += 1
                # Count the number of valid substrings that end at s[right]
                count += right - left + 1
            return count
        return atMostKDistinct(k) - atMostKDistinct(k - 1)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
    print("~")
# } Driver Code Ends