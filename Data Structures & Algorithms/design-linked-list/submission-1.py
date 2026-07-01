class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)

        # This part is creating dummy nodes so Every Isertion will be in the Middle of the List
        self.left.next = self.right
        self.right.prev = self.left

        
    def get(self, index: int) -> int:
        cur = self.left.next

        # Iterate Through to Get to the Position of the Index
        while cur != self.right and index > 0:
            cur = cur.next
            index -= 1

        # Ensure curr is not null, we havent reacehd the end of trhe LL, or 
        # the Index is Not 0 (loop exited before reaching index because it was too small to 
        # reach the Index)
        if cur != self.right and index == 0:
            return cur.val
        return -1
                  

    def addAtHead(self, val: int) -> None:

        # Create the new node with value, create the next pointer to add new node
        # to the head, create a previous pointer to point to the dummy head
        node = ListNode(val)
        next = self.left.next
        prev = self.left

        # Update the pointers of existing nodes
        next.prev = node
        prev.next = node

        # Update the pointers of new node
        node.next = next
        node.prev = prev
        

    def addAtTail(self, val: int) -> None:
        # Create new node, crete next, pointer and create previous pointer 
        # to intermediately store values.
        node = ListNode(val)
        next = self.right
        prev = self.right.prev

        # Update pointers for existing nodes
        next.prev = node
        prev.next = node

        # Update pointers for new node
        node.next = next
        node.prev = prev
        

    def addAtIndex(self, index: int, val: int) -> None:
        # Create ur pointer
        cur = self.left.next

        # Loop through until you get to the insertion index
        while cur and index > 0:
            cur = cur.next
            # prev = cur.prev.prev
            index -= 1
        
        # If Cur is NOT Null and the insertion Indexit is not 
        # Out of Bounds of the LL, insert node
        if cur != None and index == 0:
            # Create node, pointers for next and prev (temperary stores)
            node = ListNode(val)
            next = cur
            prev = cur.prev

            # Update pointer for current nodes
            next.prev = node
            prev.next = node

            # Update pointer for new node
            node.next = next
            node.prev = prev


    def deleteAtIndex(self, index: int) -> None:
        # Establish Starting position pointer for loop
        cur = self.left.next

        # Iterate through LL to get to Index
        while cur and index > 0:
            cur = cur.next
            index -= 1

        # If we are not out of bounds or at the nummy node
        # and the index is in the bounds of the LL
        if cur and cur != self.right and index == 0:
            # Updtate pointers to skip over node
            # that we cant to delete so that it can
            # go into garbage collection
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)