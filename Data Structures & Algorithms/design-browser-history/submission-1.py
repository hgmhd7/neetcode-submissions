# Constraints
# Can only return up to x
# Browser lower case

"""Create the new node"""
class NewNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = NewNode(homepage)


    def visit(self, url: str) -> None:
        self.cur.next = NewNode(url, self.cur)
        self.cur = self.cur.next


    def back(self, steps: int) -> str:
        # Do while self.cur.prev is valid so we dont end on a null node
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        
        return self.cur.val
            
        
    def forward(self, steps: int) -> str:
        
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1

        return self.cur.val

        # Time: O(1) Since the CONSTRRAINTS Limit Forward and Backward steps to 100 
        # Space: O(n) Since every time we visit a new node, it is added to the Linked List in Memory



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)