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
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         """Constraints: We can have a LL of 0, so we need to account for that"""

#         # Create an Auxilary Arry that can Store the node Values
#         auxLinkedList =  []
#         cur = head

#         # Loop through to add the current nodes to the auxLinkedList
#         while cur:     
#             auxLinkedList.append(cur)
#             cur = cur.next

#         # Reverse Traversal through the array to add the noded to an output Linked List
#         for i in range(len(auxLinkedList)-1, -1, -1):
#             if i > 0:
#                 auxLinkedList[i].next = auxLinkedList[i-1]
#             else:
#                 auxLinkedList[i].next = None

#         # Return None if the LL is Empty, otherwise, Return the Head of the LL
#         if len(auxLinkedList) == 0:
#             return None
        
#         else:
#             return auxLinkedList[-1]

#         # Time: O(n), Space = O(n)


# #################### My Efficient/ Optimal Implementation after Looking at Solution
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         # Initialize the Previous Node to the None to Turn the Hean of the LL Into the Tail
#         prev, curr = None, head

#         while curr:  # Run whilke cur is NOT Equal to Null

#             """These Two Variables Update the Pointer of the node to Reverse Direction and 
#             Stores a Temperary Reference to the Address of the Next Node that Needs to be Reversed
#             so we DO NOT Lose the Address once we Disconnect and Reverse the Link Later"""
            
#             # Store Temp
#             nxt = curr.next
#             # Change Pointer of Current node to Point in the Other Direction to Reverse
#             curr.next = prev


#             """Here we need to Create Two Pointers.  One Pointer Slideds to keeop Track of the 
#             Current Potition and Another Slides to Keep Track of the Previous Posituion.

#             We Updating the Single Pointer to Point to the Previous Position in order to 
#             REVERSE the Direction of the Pointers"""

#             # Slide the Previous and Current Pointers Forward One to Continue the LL Reveersal
#             prev = curr
#             curr = nxt

    
#         return prev #Since the Loop is Terminated at the Last Node 
#         # (curr is now False since the Ponter is Null at this Position)
#         # We can Simply Return the Node at This Position since it is the New Head

#         # Time: O(n), Space = O(1)




#################### Recursive Implementation
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """Logic is to REVERSE the REST, then Fix the Pointer for the Current Node"""
        # Just making an easier naming convention here
        cur = head

        if cur == None:
            return None
        
        newHead = cur
        if cur.next != None:
            newHead = self.reverseList(cur.next)
            cur.next.next = head
        head.next = None

        return newHead

        """
        Time O(1)
        Space O(n) since we have to put a cunctionin the call stack for every element in the LL
        """

        

        