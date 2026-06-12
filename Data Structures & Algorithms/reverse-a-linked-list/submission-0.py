# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#################### First Attempt
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         """Constraints: We can have a LL of 0, so we need to account for that"""

#         # Create an Auxilary Arry that can Store the node Values
#         auxArray =  []
#         outputArray = []
#         cur =  head

#         # Loop through to add the current nodes to the auxArray
#         while cur:     
#             auxArray.append(cur)
#             cur = cur.next

#         # Reverse Traversal through the array to add the noded to an output Linked List
#         for i in range(len(auxArray)-1, -1, -1):
#             outputArray.append(i)


#         if len(outputArray) == 0:
#             return []
        
#         else:
#             return outputArray

#         # Time: O(n), Space = O(n)


#################### AI Fixed
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """Constraints: We can have a LL of 0, so we need to account for that"""

        # Create an Auxilary Arry that can Store the node Values
        auxLinkedList =  []
        cur =  head

        # Loop through to add the current nodes to the auxLinkedList
        while cur:     
            auxLinkedList.append(cur)
            cur = cur.next

        # Reverse Traversal through the array to add the noded to an output Linked List
        for i in range(len(auxLinkedList)-1, -1, -1):
            if i > 0:
                auxLinkedList[i].next = auxLinkedList[i-1]
            else:
                auxLinkedList[i].next = None

        # Return None if the LL is Empty, otherwise, Return the Head of the LL
        if len(auxLinkedList) == 0:
            return None
        
        else:
            return auxLinkedList[-1]

        # Time: O(n), Space = O(n)


        

        