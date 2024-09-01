class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
    
        # Step 1: Initialize candidate1, candidate2, count1, count2
        candidate1, candidate2 = 0, 1
        count1, count2 = 0, 0
        
        # Step 2: First pass to find the two most frequent candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 3: Second pass to confirm the candidates
        result = []
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        if count1 > len(nums) // 3:
            result.append(candidate1)
        if count2 > len(nums) // 3:
            result.append(candidate2)
        
        return result