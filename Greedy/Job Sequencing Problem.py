'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        

class Solution:
    
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        # Step 1: Sort all jobs according to decreasing order of profit
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
        # Step 2: Find the maximum deadline among all jobs to determine the range of slots
        max_deadline = max(job.deadline for job in Jobs)
        
        # Step 3: Initialize slots (to check which slot is free) and job sequence (to store the job ids)
        slots = [-1] * max_deadline
        job_sequence = [-1] * max_deadline
        
        # Step 4: Initialize variables for counting the number of jobs done and total profit earned
        count_jobs = 0
        total_profit = 0
        
        # Step 5: Iterate through all the jobs
        for job in Jobs:
            # Find a free slot for this job (we start checking from the last possible slot)
            for j in range(min(job.deadline, max_deadline) - 1, -1, -1):
                if slots[j] == -1:  # If slot is free
                    slots[j] = job.id
                    job_sequence[j] = job.id
                    count_jobs += 1
                    total_profit += job.profit
                    break
        
        # Step 6: Return the number of jobs done and the total profit
        return count_jobs, total_profit