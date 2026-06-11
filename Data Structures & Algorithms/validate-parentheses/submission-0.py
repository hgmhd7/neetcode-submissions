class Solution:
    def isValid(self, s: str) -> bool:

        resultStack = []

        # Loop though the string to access the characters
        for braket in s:

            # Create conditionals to identify the types and directions of the characters
            if braket == '(' or  braket == '[' or braket == '{':
                resultStack.append(braket)
            else:
                if not resultStack:
                    return False
                
                top = resultStack.pop()
                if braket == ')' and top != '(':
                    return False

                if braket == ']' and top != '[':
                    return False

                if braket == '}' and top != '{':
                    return False

        return len(resultStack) == 0