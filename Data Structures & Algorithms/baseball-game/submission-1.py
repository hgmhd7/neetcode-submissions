class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # Create a result array
        resultStack = []

        # Total Counter
        total = 0


        # Loop through the input array and apply the operations
        for i in range(len(operations)):

            # Create Conditionals to satisf each of the situations when populating the auxilary array
            if operations[i] == '+':
                total += resultStack[-1]+resultStack[-2]
                resultStack.append(resultStack[-1]+resultStack[-2])
                

            elif operations[i] == 'D':
                total += 2*resultStack[-1]
                resultStack.append(2*resultStack[-1])
                

            elif operations[i] == 'C':
                total -= resultStack[-1]
                resultStack.pop()
                

            else:
                total += int(operations[i])
                resultStack.append(int(operations[i]))
                
 

        return total # Time O(n),  Space O(n) for creating the aux array/ Stack, Auxilary space of of O(1) accouting 
        # for the output.
        