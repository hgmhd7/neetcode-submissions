class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # Initialize current count and max count
        max_count = 0
        current_count = 0

        for i in range(0, len(nums)):

            if nums[i] == 1:  # Track current count
                current_count += 1
            
                # In the Parent If Consition of hitting a 1, see if the 
                # current count is greater than the max_count
                if current_count > max_count: 
                    max_count = current_count
           
            else: # Store max count and reset current counter
                current_count = 0

        return max_count # Time = O(n), Space is O(1)




        