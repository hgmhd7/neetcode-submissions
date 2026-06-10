class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # Create a result array
        resultStack = []


        # Loop through the input array and apply the operations
        for i in range(len(operations)):

            # Create Conditionals to satisf each of the situations when populating the auxilary array
            if operations[i] == '+':
                resultStack.append(resultStack[-1]+resultStack[-2])

            elif operations[i] == 'D':
                resultStack.append(2*resultStack[-1])

            elif operations[i] == 'C':
                resultStack.pop()

            else:
                resultStack.append(int(operations[i]))
        
        total = sum(resultStack)
 

        return total # Time O(n),  Space O(n) for creating the aux array/ Stack, Auxilary space of of O(1) accouting 
        # for the output.
        