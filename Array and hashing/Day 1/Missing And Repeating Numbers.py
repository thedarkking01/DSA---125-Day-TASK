#Platform=Coding Ninja , Interviewbit 
#link= https://www.naukri.com/code360/problems/missing-and-repeating-numbers_6828164?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse&leftPanelTabValue=PROBLEM

def findMissingRepeatingNumbers(a: [int]) -> [int]:
    # Write your code here 
    # Try to submit your code in O(n) Time complexity.
    N=len(a)
    repeating=0
    missing=0
    present=[False]*(N+1)

    for n in a:
        if present[n]:
            repeating=n
        else:
            present[n]=True
    
    for i in range(1,N+1):
        if not present[i]:
            missing=i
            break
    
    return [repeating,missing]