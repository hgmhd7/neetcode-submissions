class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for i in range(len(arr) - 1):  # Step though Array
            
            right_max = arr[i+1]  # Initialize right max value


            for j in range(i+1, len(arr)):  # Loop through the values to the right of i
                
                if arr[j] > right_max:  # Update max values to get the true max
                    right_max = arr[j]

            arr[i] = right_max  # Set current i index to the new max value     


        arr[-1] = -1  # Set value at last position in array to -1

        return arr  # Time O(n^2), Space O(1)