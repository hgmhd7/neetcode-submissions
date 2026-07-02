# Constraints
# Can only return up to x
# Browser lower case

"""Doubly Linked List Solution"""
# """Create the new node"""
# class NewNode:
#     def __init__(self, val, prev=None, next=None):
#         self.val = val
#         self.next = next
#         self.prev = prev


# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.cur = NewNode(homepage)


#     def visit(self, url: str) -> None:
#         self.cur.next = NewNode(url, self.cur)
#         self.cur = self.cur.next


#     def back(self, steps: int) -> str:
#         # Do while self.cur.prev is valid so we dont end on a null node
#         while self.cur.prev and steps > 0:
#             self.cur = self.cur.prev
#             steps -= 1
        
#         return self.cur.val
            
        
#     def forward(self, steps: int) -> str:
        
#         while self.cur.next and steps > 0:
#             self.cur = self.cur.next
#             steps -= 1

#         return self.cur.val

#         # Time: O(1) Since the CONSTRRAINTS Limit Forward and Backward steps to 100 
#         # Space: O(n) Since every time we visit a new node, it is added to the Linked List in Memory


"""Array Solution"""

class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0
        self.len = 1
        self.history = [homepage]


    def visit(self, url: str) -> None:
        # If we are at the last URL of the List
        if len(self.history) < self.i + 2:
            self.history.append(url)
        
        # If we ARE NOT at the Last URL of the List and 
        # Creating Another Path/ Erasing Previous Forward History
        else:
            self.history[self.i + 1] = url
        self.i += 1
        self.len = self.i+1



    def back(self, steps: int) -> str:
        # If you go negative, then you know you are at the beginning of the array
        self.i = max(self.i-steps, 0)

        return self.history[self.i]
            
        
    def forward(self, steps: int) -> str:
        self.i = min(self.i+steps, self.len-1)

        return self.history[self.i]

    # Time: O(1)/ or O(S) Since we have a Hard Constraints of 100 Steps
    # Space: O(n) Since we are storing each new visited page in the array


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)