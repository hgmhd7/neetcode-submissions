############################ MY FIRST ATTEMPT ########################
# class MinStack:

#     # Initialize the Stack
#     def __init__(self):

#         stack = []
#         self.stack = stack

        
#     # Add New Value to the Top of the Stack
#     def push(self, val: int) -> None:

#         self.stack.append(val)
        

#     # Extract Latest Value from the Stack    
#     def pop(self) -> None:

#         # Get Last Value in Stack and Remove
#         pop_val = self.stack[-1]
#         del self.stack[-1]

#         return pop_val
        
        
#     # Peep the Top Value on the Stack
#     def top(self) -> int:

#         peep_val = self.stack[-1]

#         return peep_val
        
#     # Get minimum Value from the Stack
#     # Will have to Implement a Loop where we Continuw Popping Until we
#     # have Popped the Last Value and maintain a Comparrison as we Iterate
#     # In Order to Get the Smallest Value
#     def getMin(self) -> int:

#         # Instanciate minValue to Positive Infinity and Stack upper Bound for Loop
#         minValue  = float('inf')
#         n = len(self.stack) - 1

#         # Loop Through Stack to Get Min Value
#         for i in range(0, len(self.stack), -1):

#             if self.stack[i] < minValue:
#                 minValue = self.stack[i]

#         return minValue



##############  AI Edited
# class MinStack:

#     # Initialize the Stack
#     def __init__(self):

#         stack = []

#         # AI
#         self.stack = stack
#         self.min_stack = []

        
#     # Add New Value to the Top of the Stack
#     def push(self, val: int) -> None:

#         self.stack.append(val)
        
#         # AI
#         if not self.min_stack or val <= self.min_stack[-1]:
#             self.min_stack.append(val)
        

#     # Extract Latest Value from the Stack    
#     def pop(self) -> None:

#         # Get Last Value in Stack and Remove
#         pop_val = self.stack[-1]
#         if pop_val == self.min_stack[-1]:
#             self.min_stack.pop()
#         del self.stack[-1]

#         return pop_val
        
        
#     # Peep the Top Value on the Stack
#     def top(self) -> int:

#         peep_val = self.stack[-1]

#         return peep_val
        
#     # Get minimum Value from the Stack
#     # Will have to Implement a Loop where we Continuw Popping Until we
#     # have Popped the Last Value and maintain a Comparrison as we Iterate
#     # In Order to Get the Smallest Value
#     def getMin(self) -> int:

#         return self.min_stack[-1]






# ############### Second Attampt of Brute Force Method

# class MinStack:

#     # Initialize the Stack
#     def __init__(self):

#         self.stack = []

        
#     # Add New Value to the Top of the Stack
#     def push(self, val: int) -> None:

#         self.stack.append(val)
    
        
#     # Extract Latest Value from the Stack    
#     def pop(self) -> None:

#         # Get Last Value in Stack and Remove
#         popVal = self.stack[-1]
#         del self.stack[-1]

#         return popVal

        
        
#     # Peep the Top Value on the Stack
#     def top(self) -> int:

#         return self.stack[-1]

        
#     # Get minimum Value from the Stack
#     # Will have to Implement a Loop where we Continuw Popping Until we
#     # have Popped the Last Value and maintain a Comparrison as we Iterate
#     # In Order to Get the Smallest Value
#     def getMin(self) -> int:

#         temp = []

#         minVal = self.stack[-1]

#         for i in range(len(self.stack)):

#             minVal = min(minVal, self.stack[-1])
#             temp.append(self.stack[-1])
#             self.stack.pop()

#         for i in range(len(temp)-1, -1, -1):

#             self.stack.append(temp[i])

#         return minVal



############### Attampt at O(1) Two Stack Method

class MinStack:

    # Initialize the Stack
    def __init__(self):

        # Declare a Min Val Variable
        minVal = float('inf')

        # Initialize the Stack and the MinStack
        self.stack = []
        self.minStack = []


        
    # Add New Value to the Top of the Stack
    def push(self, val: int) -> None:

        
        # If the stack is empty, initialize the minVal.  Othersise, populate
        # the minStack with the minimum of the current value or the stored minimum
        minVal = val if not self.stack else min(val, self.minStack[-1])
        
        # If we dont add to the stack AFTER declaring the minVal, it will 
        # ALWAYS default to the Else Portion
        # i.e. on the Very FIRST Push the Minstack is Empty, so 
        # you Sould NOT have a value at minStack[-1] and get an out of bounds error
        self.stack.append(val)
        
        self.minStack.append(minVal)

        
    # Extract Latest Value from the Stack    
    def pop(self) -> None:

        self.stack.pop()

        # You also have eo pop the last value in the minStack so that you can keep 
        # Track of the previous min Value if you shrink the stack
        self.minStack.pop()

        
    # Peep the Top Value on the Stack
    def top(self) -> int:

        return self.stack[-1]


    def getMin(self) -> int:

        # Return the Last Value in the minStack i.e. the smallest value
        return self.minStack[-1]








