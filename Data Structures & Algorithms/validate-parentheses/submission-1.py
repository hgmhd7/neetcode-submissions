class Solution:
    def isValid(self, s: str) -> bool:

        # # Create Stack
        # resultStack = []

        # # Loop though the string to access the characters
        # for bracket in s:

        #     # Create conditionals to identify the types and directions of the characters
        #     if bracket == '(' or  bracket == '[' or bracket == '{':
        #         resultStack.append(bracket)

        #     else:
        #         if not resultStack: # For empty result stack after finding Closing bracket (No Opening Bracket)
        #             return False
                
        #         # You are Popping to Pop the top of the stack to compare 
        #         # with the current closing bracket.
        #         top = resultStack.pop()

        #         if bracket == ')' and top != '(':
        #             return False

        #         if bracket == ']' and top != '[':
        #             return False

        #         if bracket == '}' and top != '{':
        #             return False


        # # If we DO NOT have Matching Sets of Brackets after Popping all Closing Brackets
        # # i.e. the resultStack has Left Over Unmatched Brackets, then Return False
        # return len(resultStack) == 0

        # # Time = O(n), Space O(n)







############# RETRY AGAIN FROM MEMORY  ################

        # Create an empty stacck to see the opening brackets
        resultStack = []

        # Loop thorugh string array to get traverse the brackets
        for string in s:

            # Add opening brackets to the stack 
            if string == "(" or string == "[" or string == "{":

                resultStack.append(string)


            # If we come across a closing bracket, the latest position in the stack 
            # has to be an opening bracket of the same type to Maintain the Open/ Close 
            # Order per the problem requirements
            else:
                
                # Return False is we Com Accross a Closing Bracket and 
                # there is Nothing in the resultStack.  i.e. No Opening Bracket of the 
                # same Type
                if not resultStack:
                    return False
                    
                latestBracket = resultStack.pop()

                # # Debug Check
                # print(latestBracket)

                if string == ")"  and latestBracket != "(":
                    return False

                if string == "]"  and latestBracket != "[":
                    return False

                if string == "}"  and latestBracket != "{":
                    return False


        # False if the stack has any left over values since that meand that there is not a 
        # corresponding close to every open.    
        return len(resultStack) == 0

        # Debug
        # return latestBracket
































