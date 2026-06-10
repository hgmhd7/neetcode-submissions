class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

############## BRUTE FORCE ################
        # for i in range(len(arr) - 1):  # Step though Array
            
        #     right_max = arr[i+1]  # Initialize right max value


        #     for j in range(i+1, len(arr)):  # Loop through the values to the right of i
                
        #         if arr[j] > right_max:  # Update max values to get the true max
        #             right_max = arr[j]

        #     arr[i] = right_max  # Set current i index to the new max value     


        # arr[-1] = -1  # Set value at last position in array to -1

        # return arr  # Time O(n^2), Space O(1)


        # MOST EFFICIENT

        new_max = arr[-1] # Establich Max Variable

        # Step Backwards through array and make max at current porition max 
        # of all the values to the right thus far
        for i in range(len(arr)-2, -1, -1):
            temp = arr[i]
            arr[i] = new_max
            new_max = max(new_max, temp)

        arr[-1] = -1  # Set value at last position in array to -1

        return arr  # Time: O(n), Space: O(1)
