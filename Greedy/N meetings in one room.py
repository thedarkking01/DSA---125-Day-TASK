# Platform = GFG 
# link=https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1


class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meets=[(start,end) for i in range(n)]
        meets.sort(key=lambda x: x[1])
        
        count=1
        end_time=meets[0][1]
        for i in range(1,n):
            if meets[i][0]>=end_time:
                count+=1
                end_time=meets[i][1]
        return count