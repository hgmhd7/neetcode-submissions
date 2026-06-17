# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


############################# My First Attempt
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
#         """Constraints = Linked List can be none, so have to watch out for that.
#         We can either have 2 empty LL, 1 Empty LL, or No Empty LL.  
#         So to account for this, we can add a conditional that checks which linked list actually have values"""
        

#         if list1 and not list2:
#             return list1

#         elif list2 and not list1:
#             return list2

#         elif list2 and not list1:
#             return []


#         # Loop through liked list with 2 pointers to sort.
#         else:

#             outputLL = []

#             while list1.next or list2.next:

#                 if list1.val <= list2.val:
#                     # Store the new output linked list into a single list
#                     outputLL.append[list1.val]
#                     list1.next

#                 else:
#                     outputLL.append[list2.val]
#                     list2.next

#         # Retrun new head 
#         return outputLL




############################# My Second Attempt after Hints
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
#         """Constraints = Linked List can be none, so have to watch out for that.
#         We can either have 2 empty LL, 1 Empty LL, or No Empty LL.  
#         So to account for this, we can add a conditional that checks which linked list actually have values"""

#         if list1 and not list2:
#             return list1

#         elif list2 and not list1:
#             return list2

#         elif not list2 and not list1:
#             return None


#         # Loop through liked list with 2 pointers to sort.
#         else:
#             # Here yoiu need Both a Dummy and a Node since you neeed to return 
#             #Dummy.Next to Skip the Placefiller Dummy Node later on
#             dummy = ListNode()
#             node = dummy

#             while list1 or list2:
#                 if list1.val <= list2.val:
#                     # Store the new output linked list into a single list
#                     node.next = list1
#                     list1 = list1.next

#                 else:
#                     node.next = list1
#                     list2 = list2.next

#         # Retrun new head 
#         return dummy.next



############################# My Third Attempt after Hints
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        """Constraints = Linked List can be none, so have to watch out for that.
        We can either have 2 empty LL, 1 Empty LL, or No Empty LL.  
        So to account for this, we can add a conditional that checks which linked list actually have values"""

        if list1 and not list2: # If list2 is empty
            return list1

        elif list2 and not list1: # If list1 is empty
            return list2

        elif not list2 and not list1: # If both list are empty
            return None


        # Loop through liked list with 2 pointers to sort.
        else:
            # Here you need Both a Dummy and a Node since you neeed to return 
            #Dummy.Next to Skip the Placefiller Dummy Node later on
            dummy = ListNode()
            node = dummy

            while list1 and list2: # And Condition to Stop Loop after One List is Exaughsted, Both List have to Still be Valid for Loop to Continue
                if list1.val <= list2.val:
                    node.next = list1 # Starting at Position 2 in the Aux LL since we are utilizing a Dummy at Position 1
                    list1 = list1.next # Iterate the pointer that is as the smallest value

                else:
                    node.next = list2
                    list2 = list2.next # Iterate the pointer that is as the smallest value

                node = node.next  # Iterate to the Nextg Node in the Output LL.  This is updated regardless of what pointer we put in our list

            # Above Loop has Ended meaning that One List is Exaughsted
            # Attatch the rest of the list that is not exaughsted
            node.next =  list1 if list1 else list2

        # Retrun new head 
        return dummy.next


        # Time O(n+m), Space O(1)

