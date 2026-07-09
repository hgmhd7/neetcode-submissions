# class Solution:
#     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

#         students1Count = 0
#         # students0Count = 0

#         for i in students:
#             if students[i] == 1:
#                 students1Count += 1
#             # else:
#             #     students0Count += 1

#         sandwich1Count = 0
#         # sandwhich0Count = 0

#         for i in sandwiches:
#             if sandwiches[i] == 1:
#                 sandwich1Count += 1
#             # else:
#             #     sandwhich0Count += 1
        
#         if students1Count == sandwich1Count:
#             return 0
#         elif students1Count > sandwich1Count:
#             return students1Count - sandwich1Count
#         else:
#             return sandwich1Count - students1Count



class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        studentsRem = len(students)
        studentHash = {}

        """SHORTCUT Python Function that replaces the need to count up the hashes in 
        a explicit Loop.  This essentially just abstracts away all those key value counts """
        # studentHash = Counter(students)

        for s in students:
            if s not in studentHash:
                # Initialize in sstudent hash first if 
                # Key DOES NOT Exist
                studentHash[s] = 0
            studentHash[s] += 1
        
        for s in sandwiches:
            if s in studentHash and studentHash[s] > 0:
                studentHash[s] -= 1
                studentsRem -= 1
            
            # """Since the ORDER of the Sadwhiches Matters, if there are NO Students Left
            # to Take the Current Sandwhich, then you can just Exit Loop since it is Impossible to 
            # Move On to the Next Sandwhich"""
            else:
                return studentsRem
                
        return studentsRem
            
            




        



        
        