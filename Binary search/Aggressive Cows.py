def aggressiveCows(stalls, k):
    def can_we_place(diff,stalls,k):
        count=1
        last_position=stalls[0]
        for i in range(1,len(stalls)):
            if stalls[i]-last_position>=diff:
                count+=1
                last_position=stalls[i]
            if count==k:
                return True
        return False
    
    stalls.sort()
    res=0
    low,high=0,stalls[-1]+stalls[0]
    while low<=high:
        mid=(low+high)//2
        if can_we_place(mid,stalls,k):
            res=mid
            low=mid+1
        else:
            high=mid-1
    return res


# Example usage:
print(aggressiveCows([0, 3, 4, 7, 10, 9], 4))  
print(aggressiveCows([4, 2, 1, 3, 6], 2)) 