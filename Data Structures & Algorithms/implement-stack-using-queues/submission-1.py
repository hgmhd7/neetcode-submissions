class MyStack:

    def __init__(self):
        # Initialize/ Create the que/ deck in this case (double ended queue)
        self.q = deque()    

    def push(self, x: int) -> None:
        self.q.append(x)

        """We are just pushing the new number to the front and maintaining the order of the other numbers."""
        for i in range(len(self.q)-1):
            pop = self.q.popleft()
            self.q.append(pop)   

    def pop(self) -> int:
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()