class Solution:
    def smallestpositive(self, array, n): 
        # Your code goes here  
        array.sort()
        smallestmissing=1
        for v in array:
            if v>smallestmissing:
                break
            smallestmissing+=v
        return smallestmissing
