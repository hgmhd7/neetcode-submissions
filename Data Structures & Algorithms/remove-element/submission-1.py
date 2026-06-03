class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        for i in range(0, len(nums)):

            if nums[i] == val: # If the Target Value is at the current index, replace with -

                nums[i] = '-'


        insert_index = 0 # Eatablish insert index to keep track of index for number insertion
        k = 0  # Counter for k instances

        for i in range(0, len(nums)):  # Shift non target values over to beginning of the array

            if nums[i] != '-':  # Shift elemets to the beginning of the array if they were not the target

                nums[insert_index] = nums[i]
                k += 1
                insert_index += 1
            
            

        return k  # Time O(n), Space O(1)



        