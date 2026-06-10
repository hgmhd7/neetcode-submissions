class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        # create an array of 2 time the lencth of the nums array for storage
        newArr =  [0] * (2 * len(nums))

        # Create a counter that starts at the last position of the nums array to position the 
        # concatination in th ecorrect position
        concatPosition = len(nums)

        # print(len(newArr))
        # Read the values from the nums array and store the concatinated values into the correct potition of the 
        # New Array

        
        for i in range(len(nums)):

            newArr[i] = nums[i]
            newArr[concatPosition] = nums[i]

            concatPosition+=1


        return newArr # Time: O(2n) >> O(n), Space = O(2n) >> O(n) since expected output is O(2n)

            
        